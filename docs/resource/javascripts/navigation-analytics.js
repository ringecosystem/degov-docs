(function () {
  'use strict';

  var EVENT_NAME = 'degov_docs_navigation';
  var SEARCH_HOST_SUBSTRINGS = ['google.', 'yahoo.'];
  var SEARCH_HOST_DOMAINS = ['bing.com', 'duckduckgo.com', 'baidu.com', 'yandex.com'];
  var SOCIAL_HOSTS = [
    'x.com',
    'twitter.com',
    'linkedin.com',
    'facebook.com',
    'discord.com',
    'telegram.org',
    't.me'
  ];
  var AI_REFERRER_HOSTS = [
    'chatgpt.com',
    'perplexity.ai',
    'copilot.microsoft.com',
    'gemini.google.com'
  ];

  function normalizeHost(hostname) {
    return String(hostname || '')
      .toLowerCase()
      .replace(/^www\./, '');
  }

  function normalizePathname(pathname) {
    var path = String(pathname || '/').toLowerCase();
    return path.length > 1 && path.endsWith('/') ? path.slice(0, -1) : path;
  }

  function hostMatchesDomain(hostname, candidate) {
    return hostname === candidate || hostname.endsWith('.' + candidate);
  }

  function hostMatchesDomains(hostname, candidates) {
    return candidates.some(function (candidate) {
      return hostMatchesDomain(hostname, candidate);
    });
  }

  function getChannelGroupFromReferrer(referrer, currentHost) {
    if (!referrer) return 'direct-unknown';

    var referrerUrl;
    try {
      referrerUrl = new URL(referrer);
    } catch (_error) {
      return 'direct-unknown';
    }

    var referrerHost = normalizeHost(referrerUrl.hostname);
    var current = normalizeHost(currentHost);

    if (current && referrerHost === current) return 'direct-unknown';
    if (hostMatchesDomains(referrerHost, AI_REFERRER_HOSTS)) return 'ai-search-assistant-referral';

    if (
      SEARCH_HOST_SUBSTRINGS.some(function (candidate) {
        return referrerHost.includes(candidate);
      }) ||
      hostMatchesDomains(referrerHost, SEARCH_HOST_DOMAINS)
    ) {
      return 'organic-search';
    }

    if (hostMatchesDomains(referrerHost, SOCIAL_HOSTS)) return 'social-organic';
    if (referrerHost === 'docs.degov.ai') return 'documentation-referral';
    if (referrerHost.endsWith('.degov.ai') || referrerHost === 'degov.ai') {
      return 'cross-product-degov-referral';
    }

    return 'other-external-referral';
  }

  function getTopicId(pathname) {
    var path = normalizePathname(pathname);
    if (path === '/') return 'home';
    if (path === '/faqs') return 'faqs';
    if (path.startsWith('/integration')) return 'integration';
    if (path.startsWith('/governance')) return 'governance';
    return 'other-docs';
  }

  function getTargetPathClass(pathname) {
    var path = normalizePathname(pathname);
    if (path === '/') return 'home';
    if (path === '/faqs') return 'faqs';
    if (path.startsWith('/integration')) return 'integration';
    if (path.startsWith('/governance/proposal')) return 'governance-proposal';
    if (path.startsWith('/governance/parameters')) return 'governance-parameters';
    if (path.startsWith('/governance')) return 'governance';
    return 'other-docs';
  }

  function buildDocsNavigationParams(targetHref) {
    if (!targetHref) return null;

    var targetUrl;
    try {
      targetUrl = new URL(targetHref, window.location.origin);
    } catch (_error) {
      return null;
    }

    var targetHost = normalizeHost(targetUrl.hostname);
    var currentHost = normalizeHost(window.location.hostname);
    if (targetHost !== currentHost && targetHost !== 'docs.degov.ai') return null;

    return {
      source_surface: 'docs',
      topic_id: getTopicId(window.location.pathname),
      target_path_class: getTargetPathClass(targetUrl.pathname),
      channel_group: getChannelGroupFromReferrer(document.referrer, window.location.hostname),
      locale: document.documentElement.lang || 'en'
    };
  }

  function sendDocsNavigationEvent(params) {
    if (typeof window.gtag !== 'function') return false;
    window.gtag('event', EVENT_NAME, params);
    return true;
  }

  function trackDocsNavigation(targetHref) {
    var params = buildDocsNavigationParams(targetHref);
    if (!params) return;

    var dedupeKey = [EVENT_NAME, params.topic_id, params.target_path_class].join(':');
    try {
      if (window.sessionStorage.getItem(dedupeKey)) return;
      if (sendDocsNavigationEvent(params)) {
        window.sessionStorage.setItem(dedupeKey, '1');
      }
    } catch (_error) {
      sendDocsNavigationEvent(params);
    }
  }

  document.addEventListener('click', function (event) {
    if (!(event.target instanceof Element)) return;

    var link = event.target.closest('a[href]');
    if (!link) return;
    trackDocsNavigation(link.getAttribute('href'));
  });

  window.DeGovDocsAnalytics = {
    buildDocsNavigationParams: buildDocsNavigationParams,
    getChannelGroupFromReferrer: getChannelGroupFromReferrer,
    getTargetPathClass: getTargetPathClass,
    getTopicId: getTopicId,
    eventName: EVENT_NAME
  };
})();

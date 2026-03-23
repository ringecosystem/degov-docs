---
description: "Set up a self-hosted DeGov instance using the current instructions from the main degov repository, including environment variables, DAO configuration, and startup steps."
---

# Setup Instructions

This guide mirrors the current setup flow from the main [degov repository](https://github.com/ringecosystem/degov?tab=readme-ov-file#setup-instructions), but keeps the instructions inside the DeGov docs for easier reading.

## Prerequisites

Before you begin, make sure you have:

- Git
- Docker
- Docker Compose

## 1. Clone the repository

```bash
git clone https://github.com/ringecosystem/degov.git
cd degov
```

## 2. Configure the environment

Copy the example environment file:

```bash
cp .env.example .env
```

Then edit `.env` and set the required values:

```env
DEGOV_DB_PASSWORD=your-secure-password
DEGOV_WEB_JWT_SECRET=your-jwt-secret
DEGOV_SYNC_AUTH_TOKEN=your-sync-token
CHAIN_RPC_1=https://eth-mainnet-rpc-url
```

!!! warning "Security"
    Replace placeholder secrets before deploying to any shared or production environment.

## 3. Configure your DAO

Edit `degov.yml` with your DAO settings, such as the governor address and chain ID.

For real configuration examples, review the [DeGov Registry](registry.md), which lists DAO config files from the public [degov-registry repository](https://github.com/ringecosystem/degov-registry/tree/main/daos).

## 4. Start all services

```bash
docker-compose up -d
```

This starts:

- PostgreSQL on port `5432`
- The indexer on port `4350`
- The web application on port `3000`

## 5. Access the application

Open [http://localhost:3000](http://localhost:3000) in your browser.

## Notes

- Initial sync may take time when the instance starts for the first time.
- If you need a managed deployment or custom setup, see [Launch With Assistant](launch.md).
- For the upstream source of these steps, see the official [degov README](https://github.com/ringecosystem/degov?tab=readme-ov-file#setup-instructions).

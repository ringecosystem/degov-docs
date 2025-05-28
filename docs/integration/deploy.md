# Deploy By Yourself

Deploy your own DeGov.AI instance using the [DeGov Launcher](https://github.com/ringecosystem/degov-launcher). The launcher provides a Docker Compose configuration for the simplest way to set up your own governance platform.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Docker** (v20.10 or later)
- **Docker Compose** (v2.0 or later)
- **Git** (for cloning the repository)

## Quick Start

1. **Clone the launcher repository:**
   ```bash
   git clone https://github.com/ringecosystem/degov-launcher.git
   cd degov-launcher
   ```

2. **Configure your DAO:**
   Edit the `degov.yml` file to customize your DAO's settings (see [Configuration Options](#configuration-options) below).

3. **Set up environment variables:**
   ```bash
   cp .env.sample .env
   ```
   Edit the `.env` file to update your environment variables (see [Environment Variables](#environment-variables) below).

4. **Launch your DeGov instance:**
   ```bash
   docker compose up -d
   ```

5. **Access your DAO:**
   Visit [http://localhost:3002](http://localhost:3002) to access your DAO's DeGov interface.

!!! note "Initial Sync"
    It may take some time to sync blockchain data when first starting the instance.

## Configuration Options

The `degov.yml` file is the core configuration file for your DeGov instance. Here are all the available configuration options:

### Basic DAO Information

```yaml
name: Your DAO Name
logo: "https://your-logo-url.com/logo.svg"
siteUrl: https://your-site-url.com
offChainDiscussionUrl: https://your-offchain-discussion-url.com
description: |
  A brief description of the DAO, which will be displayed on the DAO's homepage.
```

- **`name`**: Your DAO's display name
- **`logo`**: URL to your DAO's logo (SVG or PNG recommended)
- **`siteUrl`**: Your DAO's main website URL
- **`offChainDiscussionUrl`**: URL for off-chain discussions (e.g., Discord, Discourse)
- **`description`**: Multi-line description of your DAO

### Social Links

```yaml
links:
  website: https://example.com/
  twitter: https://x.com/TWITTER
  discord: https://discord.com/invite/DISCORD
  telegram: https://t.me/TELEGRAM
  github: https://github.com/GITHUB
  email: contact@example.com  # Optional
```

All social links are optional and will be displayed on your DAO's homepage.

### Wallet Configuration

```yaml
wallet:
  walletConnectProjectId: your_project_id
```

- **`walletConnectProjectId`**: Required for WalletConnect integration. Get your project ID from [WalletConnect](https://walletconnect.network/).

### Blockchain Configuration

```yaml
chain:
  name: Ethereum
  id: 1
  logo: https://icons.llamao.fi/icons/chains/rsz_ethereum.jpg
  rpcs:
    - https://ethereum-rpc.publicnode.com
  explorers:
    - https://etherscan.io/
  nativeToken:
    symbol: ETH
    priceId: ethereum
    decimals: 18
```

- **`name`**: Human-readable chain name (optional for well-known chains)
- **`id`**: Chain ID (1 for Ethereum mainnet, 5 for Goerli, etc.)
- **`logo`**: URL to chain logo
- **`rpcs`**: Array of RPC endpoints for blockchain interaction (optional for well-known chains)
- **`explorers`**: Array of block explorer URLs (optional for well-known chains)
- **`nativeToken`**:
  - **`symbol`**: Native token symbol (ETH, MATIC, etc.)
  - **`priceId`**: Price feed identifier (usually matches CoinGecko ID)
  - **`decimals`**: Token decimals (usually 18)

### Indexer Configuration

```yaml
indexer:
  endpoint: http://localhost:4350/graphql
  startBlock: 0
  # Optional configurations:
  # rpc: https://rpc.your.network
  # gateway: https://gateway.your.network
```

- **`endpoint`**: GraphQL endpoint for the indexer (default uses local instance)
- **`startBlock`**: Block number to start indexing from
- **`rpc`**: (Optional) Alternative RPC endpoint for indexer
- **`gateway`**: (Optional) SQD gateway for faster synchronization

### Core Contracts

```yaml
contracts:
  governor: "0x0000000000000000000000000000000000000000"
  governorToken:
    address: "0x0000000000000000000000000000000000000000"
    standard: ERC20  # or ERC721
  timeLock: "0x0000000000000000000000000000000000000000"
```

- **`governor`**: Address of your OpenZeppelin Governor contract
- **`governorToken`**: 
    - **`address`**: Address of your governance token contract
    - **`standard`**: Token standard (ERC20 or ERC721) - crucial for proper indexing
- **`timeLock`**: Address of your TimeLock contract

### Treasury Assets

```yaml
timeLockAssets:
  - name: FT
    contract: "0x0000000000000000000000000000000000000000"
    standard: ERC20
    priceId: FT
    logo: https://example.com/token-logo.png
  - name: NFT
    contract: "0x0000000000000000000000000000000000000000"
    standard: ERC721
    priceId: NFT
    logo: https://example.com/nft-logo.png
```

Configure assets held in your DAO's treasury:

- **`name`**: Asset display name
- **`contract`**: Token contract address
- **`standard`**: Token standard (ERC20 or ERC721)
- **`priceId`**: Price feed identifier
- **`logo`**: Asset logo URL (optional)

### Safe Accounts

```yaml
safes:
  - name: Safe Account 01
    chainId: 42161
    link: https://app.safe.global/home?safe=arb1:0x0000000000000000000000000000000000000000
  - name: Safe Account 02
    chainId: 11155111
    link: https://app.safe.global/home?safe=sep:0x0000000000000000000000000000000000000000
```

Configure Gnosis Safe accounts managed by your DAO:

- **`name`**: Safe account display name
- **`chainId`**: Chain ID where the Safe is deployed
- **`link`**: Direct link to the Safe interface

## Environment Variables

The `.env` file contains important configuration for your DeGov instance:

```bash
# Docker image versions - always use the latest stable versions
DEGOV_INDEXER_VERSION=v0.4.0
DEGOV_WEB_VERSION=v0.4.0

# Port configurations
DEGOV_INDEXER_PORT=4350
DEGOV_DB_PORT=7453
DEGOV_WEB_PORT=3002

# Security configurations
DEGOV_DB_PASSWORD=your_secure_database_password
DEGOV_WEB_JWT_SECRET=your_secure_jwt_secret
DEGOV_SYNC_AUTH_TOKEN=your_secure_sync_token
```

!!! warning "Security Important"
    - Change all default passwords and secrets before deploying
    - Use strong, randomly generated values for security tokens
    - Keep your `.env` file secure and never commit it to version control

### Available Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DEGOV_INDEXER_VERSION` | Docker image version for indexer | `v0.4.0` |
| `DEGOV_WEB_VERSION` | Docker image version for web interface | `v0.4.0` |
| `DEGOV_INDEXER_PORT` | Port for indexer GraphQL endpoint | `4350` |
| `DEGOV_DB_PORT` | Port for PostgreSQL database | `7453` |
| `DEGOV_WEB_PORT` | Port for web interface | `3002` |
| `DEGOV_DB_PASSWORD` | PostgreSQL database password | `let-me-in` |
| `DEGOV_WEB_JWT_SECRET` | JWT secret for web authentication | Random string |
| `DEGOV_SYNC_AUTH_TOKEN` | Authentication token for sync service | Random string |

## Troubleshooting

### Common Issues

1. **Port conflicts**: If ports are already in use, modify the port settings in your `.env` file
2. **Docker permissions**: Ensure your user has proper Docker permissions
3. **Memory issues**: The PostgreSQL service requires sufficient memory (1GB shared memory configured)
4. **Sync delays**: Initial blockchain synchronization can take time depending on your start block

### Checking Service Status

```bash
# Check all services
docker compose ps

# View logs for a specific service
docker compose logs indexer
docker compose logs web
docker compose logs postgres
```

### Updating Your Instance

1. **Pull latest images:**
   ```bash
   docker compose pull
   ```

2. **Update your configuration:**
   Update version numbers in `.env` file

3. **Restart services:**
   ```bash
   docker compose down
   docker compose up -d
   ```

## Support

If you encounter issues:

1. Check the [troubleshooting section](#troubleshooting) above
2. Review the logs using `docker compose logs`
3. Open an issue on the [DeGov Launcher repository](https://github.com/ringecosystem/degov-launcher/issues)
4. Join our [Telegram community](https://t.me/DeGov_AI) for community support
---
description: "Self-deploy DeGov.AI using Docker Compose - complete guide to setting up your own governance platform instance with the DeGov Launcher toolkit."
---

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

The `degov.yml` file is the core configuration file for your DeGov instance, following the explanation comments in the demo file. See the [https://github.com/ringecosystem/degov-registry/tree/main/daos](https://github.com/ringecosystem/degov-registry/tree/main/daos) for examples of existing DAOs. Feel to ask in the [DeGov community](https://t.me/DeGov_AI) for help with configuration.

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
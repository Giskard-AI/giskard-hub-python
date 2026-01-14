# OpenAPI Specifications

This directory contains OpenAPI specification files used to update the Python SDK.

## Expected File

The task referenced a new OpenAPI spec file: `20251118_134430.json`

However, this file is not present in the repository. To complete the API update task, please:

1. Place the OpenAPI spec file in this directory
2. Ensure the file follows the OpenAPI 3.0+ specification format
3. Run the SDK update process (to be documented)

## SDK Update Process

The SDK was initially generated with [Stainless](https://www.stainless.com/). To update the SDK based on a new OpenAPI spec:

1. Place the new OpenAPI spec in this directory
2. Run the appropriate Stainless command to regenerate/update the SDK code
3. Review generated changes for consistency
4. Update tests as needed
5. Update documentation (api.md) if public API surface changes

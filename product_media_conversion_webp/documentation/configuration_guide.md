# Configuration Guide for Product Media Conversion to WebP Module

## Table of Contents

1. Introduction
2. Accessing the Configuration Panel
3. Configuring WebP Conversion Settings
4. Managing Error Logs
5. Saving and Applying Changes

## 1. Introduction

This guide provides step-by-step instructions on how to configure the Product Media Conversion to WebP Module for Odoo 16 Community Edition. The module allows for the automatic conversion of product images to the WebP format, ensuring faster loading times and optimal image quality.

## 2. Accessing the Configuration Panel

To access the configuration panel for the WebP Conversion Module, follow these steps:

- Log in to your Odoo backend with administrative privileges.
- Navigate to the `Settings` menu.
- Under the `Customization` section, click on `WebP Conversion Settings`. This will open the configuration panel where you can manage the settings for image conversion.

## 3. Configuring WebP Conversion Settings

In the WebP Conversion Settings panel, you can configure the following options:

- **Conversion Trigger**: Choose when the image conversion to WebP should occur (e.g., on image upload, on demand).
- **Quality Settings**: Adjust the quality of the converted WebP images to balance between image quality and file size.
- **Fallback Options**: Configure fallback settings for browsers that do not support WebP format.

Make the necessary changes according to your preferences and requirements.

## 4. Managing Error Logs

The module provides an error logging mechanism to help identify and resolve issues during the image conversion process. To manage error logs:

- Navigate to the `WebP Conversion` module in the backend.
- Click on the `Error Logs` tab to view a list of conversion errors.
- The error log will display detailed information about each error, including timestamps and error messages.

Review the error logs to troubleshoot and resolve any issues with the image conversion process.

## 5. Saving and Applying Changes

After configuring the settings and managing error logs, ensure to save your changes:

- Click on the `Save` button at the bottom or top-right corner of the configuration panel.
- To apply the changes, you may need to restart the Odoo service or refresh the module, depending on your deployment.

For detailed instructions on restarting services or refreshing modules, please refer to the [installation_guide.md](installation_guide.md) and [troubleshooting_guide.md](troubleshooting_guide.md).

By following this configuration guide, you can effectively manage the WebP image conversion settings for your Odoo installation and ensure a smooth and efficient operation of the Product Media Conversion to WebP Module.
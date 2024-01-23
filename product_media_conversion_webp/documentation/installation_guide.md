# Product Media Conversion to WebP Module Installation Guide

## Overview
This guide provides instructions on how to install the Product Media Conversion to WebP Module for Odoo 16 Community Edition. This module is designed to optimize and convert product images to the WebP format, enhancing loading speed while maintaining the original image quality.

## Prerequisites
Before you begin the installation, ensure that you have:
- Administrative access to your Odoo server.
- Odoo 16 Community Edition installed on your server.

## Installation Steps

1. **Download the Module**
   - Navigate to https://thisis.com and download the `product_media_conversion_webp` module.

2. **Upload the Module**
   - Connect to your server via FTP/SFTP or SSH.
   - Upload the `product_media_conversion_webp` module to your Odoo addons directory, which is typically located at `/odoo/addons`.

3. **Update Module List**
   - Log in to your Odoo instance as an administrator.
   - Navigate to `Apps` and click on `Update Apps List`. You may need to remove the `Apps` filter to see this option.

4. **Install the Module**
   - In the Apps menu, search for `product_media_conversion_webp`.
   - Click on the `Install` button next to the module.

5. **Verify Installation**
   - After installation, you should see the module listed in the `Apps` menu.
   - You can now configure the module by following the configuration guide provided in `product_media_conversion_webp/documentation/configuration_guide.md`.

## Post-Installation

- After installing the module, you may need to restart your Odoo service for the changes to take effect.
- Use the following command to restart Odoo service (this may vary depending on your installation):
  ```
  sudo service odoo restart
  ```

## Troubleshooting

If you encounter any issues during the installation, refer to the troubleshooting guide provided in `product_media_conversion_webp/documentation/troubleshooting_guide.md` for common problems and solutions.

For further assistance, contact the module author or visit the module website at https://thisis.com.

## Conclusion

You have successfully installed the Product Media Conversion to WebP Module for Odoo 16 Community Edition. You can now proceed to configure the module to start optimizing and converting your product images to the WebP format.
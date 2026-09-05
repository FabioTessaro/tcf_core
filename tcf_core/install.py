import frappe


def after_install():
	configure_drive_storage()


def configure_drive_storage():
	settings = frappe.get_single("Drive Disk Settings")
	settings.enabled = 1
	settings.aws_key = frappe.conf.get("seaweedfs_access_key")
	settings.aws_secret = frappe.conf.get("seaweedfs_secret_key")
	settings.bucket = "drive-vault"
	settings.endpoint_url = frappe.conf.get("seaweedfs_endpoint")
	settings.use_drive_for_files = True
	settings.signature_version = "s3v4"
	settings.save()

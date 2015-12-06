# PentOS

#### CentOS with a collection of Penetration Tools

###### -------------------------------------------------------------
###### Start Virtual Box Setup
###### -------------------------------------------------------------
###### if installing in a VM, execute this section
###### if installing to the host, skip to next section
In the "Oracle VM VirtualBox Manager" window,
[ ]	select: New
In "Create Virtual Machine" window, 
	in the "Name" field, enter: PentOS YYYYMMDD
	in the "Type" list, select: Linux
	in the "Version" list, select: Red Hat (64-bit)
	in the "Memory size" bar, select: 2048 MB
	in the "Hard disk" options, select "Create a virtual hard disk now"
	select the "Create" button
In the "Create Virtual Hard Disk" window,
	in the "File size" bar, select 32.00 GB
	in the "Hard disk file type" options, select: VDI (VirtualBox Disk Image)
	in the "Storage on physical hard disk" options, select: Dynamically allocated
	select the "Create" button
In the "Oracle VM VirtualBox Manager" window,
	select: Settings
In the "PentOS YYYYMMDD - Settings" windows,
	from the left hand panel, select: Network
	In the right hand panel,
		verify that "Adapter 1" is enabled
		verify that "Adapter 1" is attached to "NAT"
In the "PentOS YYYYMMDD - Settings" windows,
	from the left hand panel, select: Shared Folders
	from the right hand panel, right click on "Machine folders" and select
In the "Add Share" dialog,
	Select a Folder Path ("\Users\myuser\Downloads")
	Select a Folder Name: host
	Select: Automount
	Select: Make Permanent
	Select: OK
In the "Oracle VM VirtualBox Manager" window,
	select: Start
In the "Select start-up disk" dialog,
	select the file browse icon
In the file browser, select: CentOS-6.5-x86_64-bin-DVD1
	select the "Open" button
In the "Select start-up disk" dialog,
	select the "Start" button
###### -------------------------------------------------------------
###### End Virtual Box Setup
###### -------------------------------------------------------------

###### -------------------------------------------------------------
###### Start CentOS 6 Install
###### -------------------------------------------------------------
In the "Welcome" dialog, select: Install or upgrade an existing system
In the "Disk" dialog, select: Skip
If the "Unsupported Hardware Dialog" dialog appears, select: OK

On the "CentOS 6" splash page, select: Next

On the "What language would you like to use during the installation process?" page, 
	select: English
	select: Next

On the "Select the appropriate keyboard for the system" page,
	select: U.S. English
	select: Next

On the "What type of devices will your installation involve?" page,
	select: Basic Storage Devices
	select: Next

In the "Storage Device Warning" dialog, 
	select: Yes, discard any data

On the "Please name this computer" page,
	in the Hostname field, enter: pentos-nn
	select: Next

On the "Please select the nearest city in your timezone" page,
	select a time zone
	select: Next

On the "The root account is used for administering the system" page, 
	in the "Root Password" field, enter a root password.
	in the "Confirm" field, enter a root password.
	select: Next

On the "What type of installation would you like?" page,
	select: "Use All Space"
	select: Next

In the "Writing storage configuration to disk" dialog,
	select: Write changes to disk

On the "The default installation of CentOS is minimal install" page,
	select: Desktop
	select: Next

On the "Congratulations, your CentOS install is complete" page,
	select: Reboot

###### -------------------------------------------------------------
###### End CentOS 6 Install
###### -------------------------------------------------------------

###### -------------------------------------------------------------
###### Start CentOS 6 Initial Configuration
###### -------------------------------------------------------------
On the "Welcome" page,
	select: Forward

On the "License Information" page,
	select: Yes, I agree to the License Agreement
	select: Forward

On the "Create User" page,
	in the "Username" field, enter: penne
	in the "Full Name" field, enter: Penne Pasta
	in the "Password" field, enter the penne password
	in the "Confirm Password" field, enter the penne password
	select: Forward
	
On the "Date and Time" page,
	adjust the date and time settings as desired
	select: Forward
	
On the "Kdump" page,
	select: Finish
	
In the "Changing Kdump" dialog,
	select: Yes

In the "The system must now reboot..." dialog,
	select: OK

###### -------------------------------------------------------------
###### End CentOS 6 Initial Configuration
###### -------------------------------------------------------------


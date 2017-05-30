# PentOS

#### CentOS with a collection of Penetration Tools

###### -------------------------------------------------------------
###### Start Virtual Box Setup
###### -------------------------------------------------------------
###### if installing in a VM, execute this section
###### if installing to the host, skip to next section
In the "Oracle VM VirtualBox Manager" window,
 -      select: New

In "Create Virtual Machine" window,
 -      in the "Name" field, enter: PentOS YYYYMMDD
 -      in the "Type" list, select: Linux
 -      in the "Version" list, select: Red Hat (64-bit)
 -      in the "Memory size" bar, select: 2048 MB
 -      in the "Hard disk" options, select "Create a virtual hard disk now"
 -      select the "Create" button

In the "Create Virtual Hard Disk" window,
 -      in the "File size" bar, select 64.00 GB
 -      in the "Hard disk file type" options, select: VDI (VirtualBox Disk Image)
 -      in the "Storage on physical hard disk" options, select: Dynamically allocated
 -      select the "Create" button

In the "Oracle VM VirtualBox Manager" window,
 -      select: Settings

In the "PentOS YYYYMMDD - Settings" windows,
 -      from the left hand panel, select: Network
 -      In the right hand panel,
 -              verify that "Adapter 1" is enabled
 -              verify that "Adapter 1" is attached to "NAT"

In the "PentOS YYYYMMDD - Settings" windows,
 -      from the left hand panel, select: Shared Folders
 -      from the right hand panel, right click on "Machine folders" and select "Add Shared Folder"

In the "Add Share" dialog,
 -      Select a Folder Path ("\Users\myuser\Downloads")
 -      Select a Folder Name: host
 -      Select: Automount
 -      Select: OK

In the "Oracle VM VirtualBox Manager" window,
 -      select: Start

In the "Select start-up disk" dialog,
 -      select the file browse icon

In the file browser, select: CentOS-7-x86_64-Everything-1511.iso
 -      select the "Open" button

In the "Select start-up disk" dialog,
 -      select the "Start" button

###### -------------------------------------------------------------
###### End Virtual Box Setup
###### -------------------------------------------------------------

###### -------------------------------------------------------------
###### Start CentOS 7 Install
###### -------------------------------------------------------------

In "WELCOME TO CENTOS 7" panel,
 -      Select: English
 -      Select: English (United States)
 -      Select: Continue

In "INSTALLATION SUMMARY" panel.
 -      Select "Partioning"

In the "INSTALLATION DESTINATION" panel
 -      In "Local Standard Disk", select appropriate disk
 -      In "Partionioning", select "I will configure" option
 -      In "Encryption", select "Encrypt my data"

In the "MANUAL PARTIONING" panel,
 -      In the "New CentOS 7 Installation" dialog,
 -      Select "+"

In the "ADD A NEW MOUNT POINT" dialog,
 -      enter one of the following rows for "Mount Point"
 -      enter the associated size for "Desired Capacity"
 -      select "Add mount point"

 -      32 GiB /
 -      08 GiB /home
 -      04 GiB /tmp
 -      04 GiB /var
 -      04 GiB /var/log
 -      04 GiB /var/log/audit"
 -      01 GiB /boot (ext 4, no encryption)
 -      # note the following two will rename the mount points to 'BIOS Boot' and 'swap'
 -      02 MiB /boot (BIOS Boot file system, no encryption)
 -      08 GiB /swap (swap, encryption)

After completing the assignments, select "Done"

In the "DISK ENCRYPTION PASSPHRASE" dialog,
 -      enter a "Passphrase"
 -      confirm the passphrase
 -      select "Save"

After closing the encryption dialog, 
 -      Once again in the Manual Partioning panel,
 -      select "Done

In the "SUMMARY OF CHANGES" dialog,
 -      Select "Accept Changes"

In the "INSTALLATION SUMMARY" panel,
 -      Select "Software Selection"

In the "SOFTWARE SELECTION" panel.
 -      In "Base Environment," Select "Development and Creative Workstation"
 -      In "Add-Ons for Selected Environment", select the following options
 -      - Additional Development
 -      - Compatability Libraries
 -      - Development Tools
 -      - File and Storage Server
 -      - Graphics Creation Tools
 -      - Legacy X Windows System Compatibilities
 -      - Network File System Client
 -      - Office Suite and Productivity
 -      - PHP Support
 -      - Perl for Web
 -      - Platform Development
 -      - Python
 -      - Security Tools

When all 'Add-Ons' are selected, select "Done"

In the "Installation Summary" panel, select "Begin Installation"

In the "CONFIGURATION" panel, select "ROOT PASSWORD"

In the "Root Password" panel,
 -      enter a 'root' password
 -      confirm the password
 -      select Done

In the "CONFIGURATION" panel, select "USER CREATION"
 -      Select "Create User"
 -      Enter a Full Name: Penne Pasta
 -      Enter a User name: penne
 -      Select "Make this user an administrator"
 -      Select "Require a password for this account"
 -      Enter a Password
 -      Confirm the Password
 -      (note advanced options here, for now leave alone)
 -      Select "Done"

After the software installation completes,
 -      select "Reboot"

#####---------------------------
##### Initial Setup
#####---------------------------

As the system powers up, enter the disk encryption password when prompted.

In the "INITIAL SETUP" panel,
 -      Select "LICENSE INFORMATION"

In the "LICENSE INFORMATION" panel,
 -      Select "I accept the license agreement" option
 -      Select "Done"

In the "INITIAL SETUP" panel,
 -      Select "NETWORK & HOST NAME"

In the "NETWORK & HOST NAME" panel,
 -      Select "Ethernet (enp0s3)
 -      Select "Configure"

In the "Editing enp0s3" dialog,
 -      In the "General" tab, select "Automatically connect to this network when it is available"
 -      Select "Save"

In the "NETWORK & HOST NAME" panel,
 -      Select "Done"

In the "INITIAL SETUP" panel,
 -      Select "Finish Configuration"

#####---------------------------
##### Login as Penne
#####---------------------------

Login as "Penne Pasta"

In the "Welcome" window,
 -      Select "Next"

In the "Typing" window,
 -      Select "Next"

In the "Online Accounts" window,
 -      Select "Skip"

In the "Ready to Go" window,
 -      Select "Start using CentOS Linux"

In the "Getting Started" window,
 -      select the small [x] in the upper right hand corner to close.

From the top panel Menu bar,
 -      Select: Applications > System Tools > Software Update
 -      After the software list is updated, select "Install Updates"
 -      Trust the source of the key
 -      Enter the root password

When software updates are complete, select "Quit"

Reboot

#####---------------------------
##### Configure VM Guest
#####---------------------------

If you are running in a VM, now is a good time to install "Guest Additions"
 -      Insert "Guest Addition" ISO (via menu options)
 -      Select "Run" to run the software
 -      Enter the root password
 -      Close the window.

Eject the ISO

Reboot

In the VM Devices, select "Shared Clipboard - Bidirectional"

If you are running in a VM, now is a good time to take a snapshot

#####--------------------------------
##### Install the PentOS packages
#####--------------------------------

Login as 'penne'

Open a terminal window
 -      enter: su -
 -      enter the root password
 -      enter: cd /opt
 -      enter: git clone http://github.com/cyberxml/pentos
 -      enter: cd /opt/pentos/build
 -      enter: ./pentos-build-1.sh # env config
 -      enter: ./pentos-build-2.sh # yum installs
 -      enter: ./pentos-build-3.sh # rpm installs
 -      enter: ./pentos-build-4.sh # pip installs
 -      enter: ./pentos-build-5.sh # manual installs

#####--------------------------------
##### Build the PentOS Repository
#####--------------------------------
##### this is to build the PentOS RPMs
##### you can skip this if you are just building the platform

enter: ./pentos-build-rpms.sh

#####--------------------------------
##### Configure PentOS
#####--------------------------------

When prompted, enter a password different from the root password

The command returns a password hash

Copy the password-hash and enter the following line into /etc/grub.conf

password --encrypted <password-hash>


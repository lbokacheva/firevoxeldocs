==============================
Install and Activate FireVoxel
==============================

.. |br| raw:: html

    <br />

.. _sysreqs:

System Requirements
-------------------

FireVoxel runs on 64-bit versions of Windows (Windows 7 and newer).
Windows XP and 32-bit Windows are not supported.

FireVoxel requires two **Microsoft Visual C++ redistributable packages**
that can be accessed via `Microsoft Visual C++ support page`_
and installed anywhere on your computer:

#. **Redistributable for Visual Studio 2015, 2017 and 2019**

       * On `Microsoft Visual C++ support page`_,
         scroll down to "Visual Studio 2015, 2017 and 2019"
         and download **x64: vc_redist.x64.exe**.

#. **Redistributable for Visual Studio 2013**

       * On `Microsoft Update for Visual C++ 2013`_, select
         an appropriate mirror site and download **vcredist_x64.exe**.

**Both of these packages are necessary.**
To check whether they are already installed on your computer,
go to Windows :guilabel:`Control Panel` > :guilabel:`Programs and Features`
and look for these packages on the list of currently installed programs.

.. _Microsoft Visual C++ support page: https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads

.. _Microsoft Update for Visual C++ 2013:
   https://support.microsoft.com/en-us/help/4032938/update-for-visual-c-2013-redistributable-package

Install FireVoxel
-----------------

#. Download Firevoxel \*.zip from FireVoxel website.
   By downloading and installing this software, you agree to the terms
   of FireVoxel :doc:`License <license>`. Please read the License Agreement carefully.

#. Extract all files from \*.zip into a folder named FireVoxel.
   Do not install FireVoxel within Program Files, because the Program Files protection
   may prevent FireVoxel from correctly addressing its subfolders.

#. If you already have a previously installed, working version of FireVoxel,
   extract the \*.zip to the existing FireVoxel folder
   and overwrite the old files. Done!

#. Run *FireVoxel.exe*. If you get an error message about a missing .DLL
   or redistributable (:numref:`Redist2013Reqd`),
   download and install the two Microsoft Visual C++ redistributable packages
   listed in :ref:`sysreqs`.

   .. _Redist2013Reqd:
   .. figure:: ../images/FV_Error_Redist2013Reqd.png
      :alt: Microsoft Visual C++ 2013 Redistributable is missing. See System Requirements.
      :align: center
      :scale: 100 %
      :figwidth: 70%
      :figclass: align-center

      Error message: Visual C++ (VC++) redistributable is missing.

#. Run *FireVoxel.exe* again.
   You will get an error message (:numref:`NoKeySpecifyLocation`).:
   "File FireVoxel.key not found. Would you like to specify exact location?"

   .. _NoKeySpecifyLocation:
   .. figure:: ../images/FV_Error_NoKey.png
      :alt: FireVoxel key file not found. Specify exact location?
      :align: center
      :scale: 100 %
      :figwidth: 70%
      :figclass: align-center

      Error message: FireVoxel.key is missing.
      Click "No" if you do not have this file.


   Click **No**. You will see another message showing your **12- to 15-digit Computer ID**,
   also saved to the clipboard and ready to be pasted by using :guilabel:`Ctrl` + :guilabel:`V` (:numref:`NoKeyMachineID`).

   .. _NoKeyMachineID:
   .. figure:: ../images/FV_Error_NoKeyMachineID.png
      :alt: This is your Computer ID. Use :guilabel:`Ctrl` + :guilabel:`V` to paste it into an email.
      :align: center
      :scale: 100 %
      :figwidth: 70%
      :figclass: align-center

      Message showing the Computer ID.


#. Email your Computer ID number to **hr18@nyu.edu**.
   Use :guilabel:`Ctrl` + :guilabel:`V` to paste your Computer ID into the message.
   Don’t send screenshot graphics. In the email, please also include your name,
   your place of work or study, and a brief description of your project
   for which you intend to use FireVoxel.

#. You will receive a reply email with a small file *FireVoxel.key* as an attachment.
   Save this attachment in your FireVoxel folder. You are now ready to use FireVoxel.

#. Please download and use new versions as they become available.
   When you install a new version,
   either overwrite the files in the existing FireVoxel folder,
   or extract the new version into a new folder, copy or move *FireVoxel.key*
   into this folder, and then delete the old folder.

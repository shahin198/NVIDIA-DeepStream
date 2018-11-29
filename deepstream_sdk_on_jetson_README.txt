***********************************************************************
                              README
               DEEPSTREAM SDK ON JETSON (PRE-RELEASE)
                         QUICK START GUIDE
***********************************************************************
The NVIDIA DeepStream SDK on Jetson Software Development Kit (SDK)
provides a framework for constructing GPU-accelerated video analytics
applications running within the Linux for Tegra (L4T) package on the
Jetson platform.

=======================================================================
Prerequisites
=======================================================================

This software requires:
- JetPack 3.2 / Linux for Tegra R28.2
- A Jetson TX1 or Jetson TX2 developer kit

The DeepStream SDK package includes:
- deepstream_sdk_on_jetson.tbz2
- deepstream_sdk_on_jetson_models.tbz2
- product documentation
- license file
- this README

After downloading the JetPack installer, proceed with the setup requirements
to flash the software image to your target system.

=======================================================================
Additional Components Required on the Target
=======================================================================

The following components must be installed and setup on the Jetson developer
kit:
- CUDA
- cuDNN
- TensorRT
- OpenCV4Tegra
- VisionWorks

Consult the JetPack documentation for detailed installation and setup
instructions.

=======================================================================
JetPack Setup Requirements
=======================================================================

To install JetPack on your Jetson Developer Kit, the following
requirements must be met:
- Jetson TX1 or Jetson TX2 development board cabled as follows:
  - An Ethernet cable plugged into the on-board Ethernet port.
  - An HDMI cable connecting the development board to an external HDMI
    display.
  - To connect USB peripherals such as keyboard, mouse, and USB/ethernet
    adapter for network connection, a USB hub must be connected to the
    working USB port on the system. This is NOT included in the
    developer kit.
- Host system with Ubuntu 14.04 64-bit operating system.

To install JetPack:
1. Place the Jetson development board into force recovery mode as follows:
   - With the system powered on, press and hold the RECOVERY FORCE button.
   - While depressing the RECOVERY FORCE button, press and release the
     RESET (RST) button.
   - Wait 2 seconds and release the RECOVERY FORCE button.
2. On the host system, navigate to the directory where you downloaded the
   JetPack installer and execute this command to run JetPack:
   ./JetPack-L4T-3.2-linux-x64.run
3. When prompted, select "Full" installation.
4. Proceed, as prompted, with the complete JetPack installation
   and flashing process.

The flashing procedure takes approximately 10-30 minutes depending
upon the host system.

=======================================================================
Installing DeepStream SDK on Jetson
=======================================================================

After using the JetPack installer, you are ready to install and run
DeepStream SDK on Jetson.

To install:
1. On the Jetson target development board, determine the IP address by
   executing the following command:

   $ ifconfig

2. Copy the DeepStream SDK on Jetson archive file from the host system
   to the "nvidia" user home directory on the Jetson development kit:

   $ scp DeepStream_SDK_on_Jetson_1.5_pre-release.tbz2 nvidia@$<ip_address>:~

   Where:
   - <ip_address> is the IP address as determined earlier.

3. On the Jetson development board, navigate to the DeepStream
   package and extract the contents:

   $ tar xpvf DeepStream_SDK_on_Jetson_1.5_pre-release.tbz2

4. Extract the DeepStream SDK on Jetson software into the file system:

   $ sudo tar xpvf deepstream_sdk_on_jetson.tbz2 -C /
   $ sudo tar xpvf deepstream_sdk_on_jetson_models.tbz2 -C /

5. Execute the following command on the Jetson development board:
   $ sudo ldconfig

6. Confirm that the DeepStream installation is successful by executing
   this command on the Jetson development board:

   $ nvgstiva-app -c ${HOME}/configs/PGIE-FP16-CarType-CarMake-CarColor.txt

=======================================================================
Running the Sample Application
=======================================================================

To run the sample application with a custom input stream:

- Execute this command using the -i option and an absolute path to the
  stream file:

  $ nvgstiva-app -c ${HOME}/configs/PGIE-FP16-CarType-CarMake-CarColor.txt \
    -i <path_to_input_stream>

To run the sample application using the graphical user interface:

  $ nvgstiva-app-gui -c ${HOME}/configs/PGIE-FP16-CarType-CarMake-CarColor.txt \
    -i <path_to_input_stream> -g ${HOME}/configs/gui_cfg.txt

- If the error 'Failed to create pipeline' is displayed, remove the cache
  files on the Jetson developer kit as follows:

  $ sudo rm -rf ${HOME}/.cache/*

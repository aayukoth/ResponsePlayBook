# ADB Utility Tool

ADB Utility Tool is a software that aims to increase the productivity of the user's running ADB from the CLI by providing a GUI option.  
Apart from that the tool is highly customizable and the users can exploit the various features provided as below 
- List all connected devices
- Execute ADB commands (for multiple devices)
- Save Logs for multiple devices on given path
- Filtering the Logs
- Screenshot and Screen recording
- Drag & drop to push files or install APK
- Dedicated terminal for each device
- scrcpy
- Customizable buttons

# Getting Started

1.	Installation process  
Users can unzip the [ADB Utility Tool.zip](https://microsoft.sharepoint.com/:u:/r/teams/AMPXPlatform/Shared%20Documents/OSServices/ADB%20Utility%20Tool/ADB%20Utility%20Tool.zip?csf=1&web=1&e=66eyFC) and run `ADBToolUI.exe`  
2.	Software dependencies
- [adb](https://developer.android.com/tools/adb)  
- [python](https://www.python.org/downloads/windows/)
- [scrcpy](https://github.com/Genymobile/scrcpy/blob/master/doc/windows.md)

# Build and Test

Users also build the application from the source by following the below steps  
1. Get [Visual Studio](https://visualstudio.microsoft.com/downloads/) and [.NET 6](https://dotnet.microsoft.com/en-us/download)  
2. Clone the [project repo](https://dev.azure.com/E-OS/osservices/_git/ADB-Util-Tool) and open `ADB Utility Tool.sln` located inside the `src` directory using the Solution Explorer.  
![image.png](/.attachments/image-3b65d340-0f44-4ac9-a111-9d719c1eb865.png)
3. Users can now select `ADBToolUI` from the drop-down option and press `Ctrl+Shift+B` to build the project.  
![image.png](/.attachments/image-f9c39fd8-9d92-47ee-971a-b311a60b1fe8.png)

To run the test cases, users can right-click on `ADBToolLibrary.Tests` and click on `Run Tests`   
![image.png](/.attachments/image-bcc8ff23-008a-41e3-8868-c31028f113c8.png)

# References
- [Project Repo](https://dev.azure.com/E-OS/osservices/_git/ADB-Util-Tool)
- [SRS](https://microsoft.sharepoint.com/:w:/r/teams/AMPXPlatform/Shared%20Documents/OSServices/ADB%20Utility%20Tool/SRS.docx?d=wa01d7f31c3d048c3bce7116b8dae3308&csf=1&web=1&e=3EeTDR) (Software Requirements Specification) 
- [SDD](https://microsoft.sharepoint.com/:w:/r/teams/AMPXPlatform/Shared%20Documents/OSServices/ADB%20Utility%20Tool/SRS.docx?d=wa01d7f31c3d048c3bce7116b8dae3308&csf=1&web=1&e=3EeTDR) (Software Design Document)
- [Presentation](https://microsoft.sharepoint.com/:w:/r/teams/AMPXPlatform/Shared%20Documents/OSServices/ADB%20Utility%20Tool/SRS.docx?d=wa01d7f31c3d048c3bce7116b8dae3308&csf=1&web=1&e=3EeTDR) and [Recording](https://microsoft.sharepoint.com/:v:/r/teams/AMPXPlatform/Shared%20Documents/OSServices/ADB%20Utility%20Tool/Intern%20final%20presentation-20230705_140231-Meeting%20Recording.mp4?csf=1&web=1&e=lzegj2)
- [Pre-built Application](https://microsoft.sharepoint.com/:u:/r/teams/AMPXPlatform/Shared%20Documents/OSServices/ADB%20Utility%20Tool/ADB%20Utility%20Tool.zip?csf=1&web=1&e=66eyFC)
- [Tool Demo](https://microsoft.sharepoint.com/:v:/r/teams/AMPXPlatform/Shared%20Documents/OSServices/ADB%20Utility%20Tool/ADB_Util_Tool_Demo.mp4?csf=1&web=1&e=fQcXqd)
# LunaHR - Heart rate to VRChat through OSC 

If you like my project, please star it as it shows you're interested! <3

#### Please direct issues to me, I'd love to fix any.

## Setup:

### Avatar
The needed prefabs is in LunaHR.unitypackage. Avatar setup is as simple as any other VRCFury asset, and should be drag and drop onto your avatar.

Before importing LunaHR.unitypackage, please make sure you already have Poiyomi Toon (or Poi Pro) installed.
Alternatively, if you do not want to use Poi, you'd lack the BPM effect unless you set it up yourself.
This is slightly time consuming, but overall worth it.

*HR Prefab should be dragged onto the avatar root itself.*

VRCFury should take care of all setup from this point. If not, please contact me because then I'd need to fix some things.

### Polar H10
The main Polar H10 script is set up to work with specifically my device, and may not work with yours without tweaking "HEART_RATE_UUID" and "POLAR_H10_NAME" within the script.

### Pulsoid
Replace "YOUR_ACCESS_TOKEN_HERE" in the pulsoidHROSC script with your token. A token requires Pulsoid's "BRO" plan and can be found at https://pulsoid.net/ui/keys

## Credits and info
HEAVILY inspired by the (now inactive) project here: https://github.com/200Tigersbloxed/HRtoVRChat_OSC/

This project does NOT use the same parameters as the one by 200Tigersbloxed.
This is both because they're not meant to be the same, nor compatible, and also becuase everything in that project is outdated and the Unity files doesn't really work properly anymore.
*Feel free to use mine as a (semi-)direct replacement.*

The heart and text uses Poiyomi Toon, which you can get from Poi's Discord. https://discord.gg/poiyomi

OSC port (AND VRCHAT IP) can be changed in the scripts as well.

Unity files are set up to work with my personal avatar, thus getting it to work on your own might take some tinkering. (I am not sure.)
#PY  <- Needed to identify #
#--automatically built--

adm = Avidemux()
adm.loadVideo("H:/0821/20240821124153_0060.mp4")
adm.appendVideo("H:/0821/20240821124251_0060.mp4")
adm.appendVideo("H:/0821/20240821124351_0060.mp4")
adm.appendVideo("H:/0821/20240821124451_0060.mp4")
adm.appendVideo("H:/0821/20240821124551_0060.mp4")
adm.appendVideo("H:/0821/20240821124651_0060.mp4")
adm.appendVideo("H:/0821/20240821124751_0060.mp4")
adm.appendVideo("H:/0821/20240821124851_0060.mp4")
adm.appendVideo("H:/0821/20240821124951_0060.mp4")
adm.appendVideo("H:/0821/20240821125052_0055.mp4")
adm.appendVideo("H:/0821/20240821132539_0060.mp4")
adm.appendVideo("H:/0821/20240821132638_0060.mp4")
adm.appendVideo("H:/0821/20240821132738_0009.mp4")
adm.appendVideo("H:/0821/20240821141637_0060.mp4")
adm.appendVideo("H:/0821/20240821141736_0060.mp4")
adm.appendVideo("H:/0821/20240821141836_0060.mp4")
adm.appendVideo("H:/0821/20240821141937_0060.mp4")
adm.appendVideo("H:/0821/20240821142037_0060.mp4")
adm.appendVideo("H:/0821/20240821142137_0032.mp4")
adm.appendVideo("H:/0821/20240821143924_0060.mp4")
adm.appendVideo("H:/0821/20240821144024_0060.mp4")
adm.appendVideo("H:/0821/20240821144124_0060.mp4")
adm.appendVideo("H:/0821/20240821144224_0060.mp4")
adm.appendVideo("H:/0821/20240821144324_0060.mp4")
adm.appendVideo("H:/0821/20240821144424_0060.mp4")
adm.appendVideo("H:/0821/20240821144524_0060.mp4")
adm.appendVideo("H:/0821/20240821144624_0060.mp4")
adm.appendVideo("H:/0821/20240821144724_0060.mp4")
adm.appendVideo("H:/0821/20240821144824_0060.mp4")
adm.appendVideo("H:/0821/20240821144924_0060.mp4")
adm.appendVideo("H:/0821/20240821145025_0060.mp4")
adm.appendVideo("H:/0821/20240821145125_0060.mp4")
adm.appendVideo("H:/0821/20240821145225_0040.mp4")
adm.appendVideo("H:/0821/20240821174006_0009.mp4")

adm.setHDRConfig(1, 1, 1, 1, 0)
adm.videoCodec("Copy")
adm.audioClearTracks()
adm.setSourceTrackLanguage(0,"eng")
if adm.audioTotalTracksCount() <= 0:
    raise("Cannot add audio track 0, total tracks: " + str(adm.audioTotalTracksCount()))
adm.audioAddTrack(0)
adm.audioCodec(0, "copy")
adm.audioSetDrc2(0, 0, 1, 0.001, 0.2, 1, 2, -12)
adm.audioSetEq(0, 0, 0, 0, 0, 880, 5000)
adm.audioSetChannelGains(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
adm.audioSetChannelDelays(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
adm.audioSetChannelRemap(0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8)
adm.audioSetShift(0, 0, 0)
adm.setContainer("MKV", "forceAspectRatio=False", "displayWidth=1280", "displayAspectRatio=2", "addColourInfo=False", "colMatrixCoeff=2", "colRange=0", "colTransfer=2", "colPrimaries=2")
#! /usr/bin/env python3

import os

#################### 用户配置 ###################

# 项目路径
projectPath = ''

# 项目bundleID
projectBundleID = ''

# provisioningfile
provisioningName = ''

# Certificatefile
CertificateName = ''

# 项目名称
projectName = ''

# 打包路径
IpaSavePath = ''

# exportOptionPlist文件路径 此项可选填
exportOptionPlistPath = ''

################# 配置以上参数 ####################

# 生成的Archive文件的路径
archivePath = IpaSavePath + '/' + projectName

# 创建plist文件
def createPlist():
    global exportOptionPlistPath
    if exportOptionPlistPath == '':
        print('####正在创建plist文件####')
        os.system("echo '<?xml version='1.0' encoding='UTF-8'?><!DOCTYPE plist PUBLIC '-//Apple//DTD PLIST 1.0//EN' 'http://www.apple.com/DTDs/PropertyList-1.0.dtd'><plist version='1.0'><dict/></plist>' > exportOption.plist")
        os.system("plutil -lint exportOption.plist")
#        os.system("plutil -insert compileBitcode -bool 'NO' exportOption.plist")
        os.system("plutil -insert method -string '' exportOption.plist")
        os.system("plutil -insert provisioningProfiles -json '{\"%s\":\"%s\"}' exportOption.plist" % (projectBundleID, provisioningName))
        os.system("plutil -insert signingCertificate -string 'iPhone Distribution' exportOption.plist")
        os.system("plutil -insert signingStyle -string 'manual' exportOption.plist")
        os.system("plutil -insert stripSwiftSymbols -bool 'YES' exportOption.plist")
        os.system("plutil -insert teamID -string %s exportOption.plist" % CertificateName)
        os.system("plutil -insert uploadSymbols -bool 'YES' exportOption.plist")
        exportOptionPlistPath = projectPath + '/' + 'exportOption.plist'
        print(exportOptionPlistPath)

# 确定打包样式
def makeSureConfiguration():
    res = input('###是否要打包Debug版本,如果是请输入1###\n')
    if res == '1' :
        return 'Debug'
    return 'Release'

# 生成archive文件
def makeArchive(str):
    print(str)
    os.system('xcodebuild archive -workspace %s.xcworkspace -scheme %s -configuration %s -archivePath %s'%(projectName,projectName,str,archivePath))


# 生成iPa包
def makeIpa():
    os.system('xcodebuild -exportArchive -archivePath %s.xcarchive -exportPath %s -exportOptionsPlist %s'%(archivePath,IpaSavePath,exportOptionPlistPath))

# 自动打包
def automaticPack():
    createPlist()
    con = makeSureConfiguration()
    makeArchive(con)
    makeIpa()
    print('打包成功！')

automaticPack()































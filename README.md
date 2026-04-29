# 🛡️ Sec_search — 网络安全信息搜集指南

> 一份系统化的网络安全信息搜集资源汇总，涵盖漏洞情报、威胁情报、工具、社区与学习资源。

---

## 📌 目录

- [简介](#简介)
- [漏洞信息来源](#漏洞信息来源)
- [威胁情报平台](#威胁情报平台)
- [安全资讯与博客](#安全资讯与博客)
- [搜索引擎与指纹识别](#搜索引擎与指纹识别)
- [漏洞利用数据库](#漏洞利用数据库)
- [恶意样本分析](#恶意样本分析)
- [CTF 资源](#ctf-资源)
- [安全社区与论坛](#安全社区与论坛)
- [学习资源](#学习资源)
- [工具集合](#工具集合)
- [国内安全资源](#国内安全资源)
- [贡献指南](#贡献指南)

---

## 简介

本项目旨在系统性地整理网络安全信息搜集的方向与渠道，帮助安全研究人员、渗透测试工程师、CTF 选手以及安全爱好者快速定位有价值的信息源，提升信息搜集效率。

---

## 漏洞信息来源

### 国际权威数据库

| 名称 | 地址 | 说明 |
|------|------|------|
| NVD (美国国家漏洞数据库) | https://nvd.nist.gov/ | 美国政府官方 CVE 信息库，包含 CVSS 评分 |
| CVE Details | https://www.cvedetails.com/ | CVE 可视化查询平台，支持按厂商、产品筛选 |
| MITRE CVE | https://cve.mitre.org/ | CVE 编号官方申请与查询 |
| OSV (Open Source Vulnerabilities) | https://osv.dev/ | 开源软件漏洞数据库，由 Google 维护 |
| VulDB | https://vuldb.com/ | 实时更新的漏洞跟踪平台 |

### 国内权威数据库

| 名称 | 地址 | 说明 |
|------|------|------|
| CNVD (国家信息安全漏洞共享平台) | https://www.cnvd.org.cn/ | 国内官方漏洞平台 |
| CNNVD (国家信息安全漏洞库) | https://www.cnnvd.org.cn/ | 中国信息安全测评中心维护 |
| OSCS (开源安全社区) | https://www.oscs1024.com/ | 开源软件供应链安全情报 |

---

## 威胁情报平台

| 名称 | 地址 | 说明 |
|------|------|------|
| VirusTotal | https://www.virustotal.com/ | 文件、URL、IP 多引擎检测 |
| AlienVault OTX | https://otx.alienvault.com/ | 开放威胁情报共享社区 |
| Shodan | https://www.shodan.io/ | 全球联网设备搜索引擎 |
| Censys | https://censys.io/ | 互联网资产扫描与分析 |
| ThreatBook (微步在线) | https://x.threatbook.com/ | 国内领先威胁情报平台 |
| 奇安信威胁情报中心 | https://ti.qianxin.com/ | 奇安信旗下威胁情报平台 |
| 安恒威胁情报中心 | https://ti.dbappsecurity.com.cn/ | 安恒信息威胁情报 |
| MISP | https://www.misp-project.org/ | 开源威胁情报共享平台 |
| AbuseIPDB | https://www.abuseipdb.com/ | IP 恶意行为报告数据库 |
| GreyNoise | https://www.greynoise.io/ | 区分互联网背景噪音与真实威胁 |

---

## 安全资讯与博客

### 英文资讯

| 名称 | 地址 | 说明 |
|------|------|------|
| The Hacker News | https://thehackernews.com/ | 网络安全新闻聚合 |
| Krebs on Security | https://krebsonsecurity.com/ | 知名安全记者 Brian Krebs 的博客 |
| Bleeping Computer | https://www.bleepingcomputer.com/ | 技术安全新闻 |
| Dark Reading | https://www.darkreading.com/ | 企业安全媒体 |
| SecurityWeek | https://www.securityweek.com/ | 信息安全新闻 |
| Threatpost | https://threatpost.com/ | 安全威胁资讯 |
| SANS Internet Storm Center | https://isc.sans.edu/ | 每日安全事件报告 |

### 中文资讯

| 名称 | 地址 | 说明 |
|------|------|------|
| 安全客 | https://www.anquanke.com/ | 国内综合安全资讯平台 |
| FreeBuf | https://www.freebuf.com/ | 国内知名安全社区与资讯 |
| 嘶吼 RoarTalk | https://www.4hou.com/ | 国内安全攻防资讯 |
| 先知社区 | https://xz.aliyun.com/ | 阿里云旗下安全技术社区 |
| 奇安信 CERT | https://cert.qianxin.com/ | 漏洞预警与安全公告 |
| 绿盟科技博客 | https://blog.nsfocus.net/ | 绿盟安全研究团队博客 |

---

## 搜索引擎与指纹识别

| 名称 | 地址 | 说明 |
|------|------|------|
| Shodan | https://www.shodan.io/ | 互联网设备搜索，支持 Banner 检索 |
| Censys | https://search.censys.io/ | 证书、IP、域名综合搜索 |
| FOFA | https://fofa.info/ | 国内网络空间测绘引擎 |
| Hunter (鹰图) | https://hunter.qianxin.com/ | 奇安信旗下测绘引擎 |
| ZoomEye (钟馗之眼) | https://www.zoomeye.org/ | 知道创宇旗下空间搜索引擎 |
| Quake | https://quake.360.net/ | 360 旗下网络空间测绘 |
| FullHunt | https://fullhunt.io/ | 攻击面管理与资产发现 |
| LeakIX | https://leakix.net/ | 暴露服务与数据泄漏检测 |
| Netlas | https://netlas.io/ | 网络资产搜索引擎 |

---

## 漏洞利用数据库

| 名称 | 地址 | 说明 |
|------|------|------|
| Exploit-DB | https://www.exploit-db.com/ | 漏洞利用代码归档，由 Offensive Security 维护 |
| Packet Storm | https://packetstormsecurity.com/ | 安全工具与漏洞利用存档 |
| Sploitus | https://sploitus.com/ | 漏洞利用与工具聚合搜索 |
| GitHub Advisory Database | https://github.com/advisories | GitHub 维护的安全公告数据库 |
| Vulhub | https://vulhub.org/ | Docker 漏洞环境一键搭建 |
| nuclei-templates | https://github.com/projectdiscovery/nuclei-templates | 大量漏洞检测模板 |

---

## 恶意样本分析

| 名称 | 地址 | 说明 |
|------|------|------|
| VirusTotal | https://www.virustotal.com/ | 文件多引擎扫描 |
| Any.Run | https://any.run/ | 在线交互式沙箱 |
| Hybrid Analysis | https://www.hybrid-analysis.com/ | 免费恶意软件分析服务 |
| MalwareBazaar | https://bazaar.abuse.ch/ | 恶意样本共享数据库 |
| Joe Sandbox | https://www.joesandbox.com/ | 深度行为分析沙箱 |
| Cuckoo Sandbox | https://cuckoosandbox.org/ | 开源自动化恶意软件分析 |
| URLScan | https://urlscan.io/ | URL 安全扫描与截图 |
| Triage | https://tria.ge/ | 恶意软件自动化分析平台 |

---

## CTF 资源

### 题目平台

| 名称 | 地址 | 说明 |
|------|------|------|
| CTFtime | https://ctftime.org/ | 全球 CTF 赛事日历与战队排名 |
| Hack The Box | https://www.hackthebox.com/ | 在线渗透测试练习平台 |
| TryHackMe | https://tryhackme.com/ | 适合入门的 CTF 与靶机学习平台 |
| PicoCTF | https://picoctf.org/ | 面向初学者的 CTF 竞赛平台 |
| BUUCTF | https://buuoj.cn/ | 国内综合 CTF 题库 |
| NSSCTF | https://www.nssctf.cn/ | 国内 CTF 练习与比赛平台 |
| pwn.college | https://pwn.college/ | 专注于二进制安全的学习平台 |
| CryptoHack | https://cryptohack.org/ | 密码学挑战学习平台 |

### WriteUp 资源

| 名称 | 地址 | 说明 |
|------|------|------|
| CTF Writeups (GitHub) | https://github.com/ctfs | 历届 CTF WriteUp 汇总 |
| 先知社区 CTF 专区 | https://xz.aliyun.com/ | 国内 CTF WriteUp 分享 |

---

## 安全社区与论坛

| 名称 | 地址 | 说明 |
|------|------|------|
| Reddit r/netsec | https://www.reddit.com/r/netsec/ | 英文安全技术讨论社区 |
| HackerOne | https://www.hackerone.com/ | 漏洞赏金平台 |
| Bugcrowd | https://www.bugcrowd.com/ | 漏洞赏金与渗透测试平台 |
| 先知社区 | https://xz.aliyun.com/ | 国内安全技术交流 |
| 吾爱破解 | https://www.52pojie.cn/ | 逆向与破解技术交流 |
| 看雪安全 | https://bbs.kanxue.com/ | 国内逆向与漏洞研究论坛 |
| 安全脉搏 | https://www.secpulse.com/ | 安全文章与技术分享 |

---

## 学习资源

### 在线课程与文档

| 名称 | 地址 | 说明 |
|------|------|------|
| OWASP | https://owasp.org/ | Web 应用安全标准与文档 |
| MITRE ATT&CK | https://attack.mitre.org/ | 攻击者战术与技术知识库 |
| Cybrary | https://www.cybrary.it/ | 网络安全在线学习平台 |
| PortSwigger Web Security Academy | https://portswigger.net/web-security | 免费 Web 安全实战课程 |
| HackTricks | https://book.hacktricks.xyz/ | 渗透测试技巧手册 |
| GTFOBins | https://gtfobins.github.io/ | Linux 权限提升与绕过技巧 |
| LOLBAS | https://lolbas-project.github.io/ | Windows 原生工具利用技巧 |

### 推荐书籍

- 《Web安全攻防：渗透测试实战指南》
- 《黑客与画家》
- 《The Web Application Hacker's Handbook》
- 《Penetration Testing》by Georgia Weidman
- 《恶意代码分析实战》
- 《计算机病毒与恶意代码》

---

## 工具集合

### 信息搜集

| 工具 | 说明 |
|------|------|
| [Nmap](https://nmap.org/) | 端口扫描与服务识别 |
| [Masscan](https://github.com/robertdavidgraham/masscan) | 超高速端口扫描 |
| [subfinder](https://github.com/projectdiscovery/subfinder) | 子域名枚举 |
| [amass](https://github.com/owasp-amass/amass) | 网络攻击面资产发现 |
| [httpx](https://github.com/projectdiscovery/httpx) | HTTP 探测工具 |
| [whatweb](https://github.com/urbanadventurer/WhatWeb) | Web 指纹识别 |
| [theHarvester](https://github.com/laramies/theHarvester) | 邮箱、域名、IP 信息搜集 |

### 漏洞扫描

| 工具 | 说明 |
|------|------|
| [Nuclei](https://github.com/projectdiscovery/nuclei) | 基于模板的快速漏洞扫描 |
| [Nikto](https://github.com/sullo/nikto) | Web 服务器漏洞扫描 |
| [SQLMap](https://sqlmap.org/) | SQL 注入自动化检测 |
| [AWVS](https://www.acunetix.com/) | Web 漏洞扫描商业工具 |
| [OpenVAS](https://www.openvas.org/) | 开源综合漏洞扫描 |

### 渗透测试框架

| 工具 | 说明 |
|------|------|
| [Metasploit](https://www.metasploit.com/) | 最流行的渗透测试框架 |
| [Cobalt Strike](https://www.cobaltstrike.com/) | 红队攻击模拟平台 |
| [Burp Suite](https://portswigger.net/burp) | Web 渗透测试利器 |
| [OWASP ZAP](https://www.zaproxy.org/) | 开源 Web 安全扫描代理 |

---

## 国内安全资源

### 应急响应与通告

| 名称 | 地址 | 说明 |
|------|------|------|
| CNCERT/CC | https://www.cert.org.cn/ | 国家互联网应急中心 |
| 工信部网络安全威胁信息共享平台 | https://www.miit-cybersec.org.cn/ | 工信部官方平台 |
| 国家互联网信息办公室 | http://www.cac.gov.cn/ | 互联网监管政策发布 |

### 安全厂商博客

| 名称 | 地址 | 说明 |
|------|------|------|
| 360 安全客 | https://www.anquanke.com/ | 360 安全研究成果 |
| 腾讯安全应急响应中心 | https://security.tencent.com/ | 腾讯 SRC |
| 阿里云安全 | https://security.alibaba.com/ | 阿里 SRC |
| 百度安全应急响应中心 | https://bsrc.baidu.com/ | 百度 SRC |
| 华为安全应急响应中心 | https://isrc.huawei.com/ | 华为 SRC |

---

## 贡献指南

欢迎提交 Issue 或 Pull Request 来完善本项目！

- 提交新的信息来源时请附上简要说明
- 确保链接可访问且内容安全合规
- 遵守相关法律法规，合理合法使用安全信息

---

> ⚠️ **免责声明**：本项目仅用于安全研究与学习目的，所有内容均来自公开信息源。使用者需遵守所在地区的法律法规，严禁将相关资源用于非法活动。

---

<p align="center">
  <img src="https://img.shields.io/badge/安全研究-信息搜集-blue" />
  <img src="https://img.shields.io/badge/持续更新-欢迎贡献-green" />
  <img src="https://img.shields.io/badge/license-MIT-orange" />
</p>
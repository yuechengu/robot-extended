# Robot Framework Extended

基于Python脚本驱动的Robot Framework框架

@author: JiangTao-TeamB

## Git工程目录

- `cases`：套件和用例（基于py脚本，robot脚本运行时自动生成）
- `cfg`：配置文件
- `data`：excel文件
- `extend`: Robot Framework扩展库
- `library`: 自定义库
- `reports`: 执行结果报告

## 安装
```bash
# 运行前确保已下载以下库
pip install openpyxl -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

pip install robotframework -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

pip install --upgrade robotframework-seleniumlibrary
```

## 运行

### Q1 自动提交销售数据

```bash
# 运行套件Q1
run --suite 自动提交
```

### Q2 自动采集疫情数据

```bash
# 运行套件Q2
run --suite 自动采集
```

### Q3 爬取自如房源数据

```bash
# 运行套件Q3
run --suite 租房信息
```
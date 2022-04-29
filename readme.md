## Robot Framework Extended

基于Python脚本驱动的Robot Framework框架

author: yuechen.gu

## 题目案例
### 安装
```bash
# 运行前确保已下载以下库
pip install openpyxl -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

pip install robotframework -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

pip install --upgrade robotframework-seleniumlibrary
```

### 运行
```bash
# 所有case一起运行
run
```

### Q1 自动提交销售数据

```bash
# 单独运行套件Q1
run --suite 自动提交
```

### Q2 自动采集疫情数据

```bash
# 单独运行套件Q2
run --suite 自动采集
```
D:\shell\CygWin\cygwin64\bin\mintty.exe -h always -e /bin/bash -li -c 'ssh -X pi@192.168.1.124
!22342234
cd ~/Toch/toch_mpy/
vim i2c_com.py
vim i2c_rpi_driver.py


python3 2simb01.py 
python3 i2c_com.py i2c_2s

python3 i2c_com.py i2c_sar_l

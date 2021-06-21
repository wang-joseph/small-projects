import requests, lxml, time, subprocess, sys
from bs4 import BeautifulSoup

from secrets import websites
# yeah i'm not using a proper dotenv, but sue me ok


running = True
info = "cringe"

ok = '\033[96m'
enc = '\033[0m'
fail = '\033[91m'

while running:
    for website in websites:
        if not running:
            break

        page = requests.get(website)
        if page.status_code == 200:
            soup = BeautifulSoup(page.text, 'lxml')

            index = 1
            while (total := soup.find_all(id=f'ctl00_ctlSearchLayout_ctl00_ctl01_ctlIPGridView_GridViewRow{index}_Label_numberopenings_{index}')) != []:
                if total[0].string != "0":
                    website = soup.find_all(id=f'ctl00_ctlSearchLayout_ctl00_ctl01_ctlIPGridView_GridViewRow{index}_Label_name_{index}')[0]
                    info = ""
                    for string in website.stripped_strings:
                        info += repr(string) + " "

                    running = False
                    sys.stdout.write(f"{ok}Found one!! {info}\n{enc}")
                    break

                index += 1
    
    if running:
        sys.stdout.write(f"{fail}Still empty. \n{enc}")
        time.sleep(10)
    else:
        command = (
            f'Add-Type -AssemblyName System.Windows.Forms \n'
            f'Add-Type -AssemblyName System.Windows.Forms \n'
            f'$global:balloon = New-Object System.Windows.Forms.NotifyIcon \n'
            f'$path = (Get-Process -id $pid).Path \n'
            f'$balloon.Icon = [System.Drawing.Icon]::ExtractAssociatedIcon($path) \n'
            f'$balloon.BalloonTipIcon = [System.Windows.Forms.ToolTipIcon]::Warning \n'
            f"$balloon.BalloonTipText = '{info} OMG GO GO GO' \n"
            f'$balloon.BalloonTipTitle = "VACCINEEEEEE" \n'
            f'$balloon.Visible = $true \n'
            f'$balloon.ShowBalloonTip(10000) \n'
        )

        subprocess.run(['powershell', '-Command', command], capture_output=True)
        running = True


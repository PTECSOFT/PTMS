import ptlib

hostname= ptlib.shell('uname -a').split(' ')[1]
print('configuring for hostname: '+hostname)

if hostname=='yuri':
    class config:
        hostname = ptlib.shell('uname -a').split(' ')[1]
        cpu_temp='/sys/class/thermal/thermal_zone0/temp'
        fan_speed=(False, '')
        fan_speed_max=255
        battery='/sys/class/power_supply/BAT1/capacity'
        battery_status='/sys/class/power_supply/BAT0/status'
elif hostname=='stalin':
    class config:
        hostname = ptlib.shell('uname -a').split(' ')[1]
        cpu_temp='/sys/class/thermal/thermal_zone0/temp'
        fan_speed='/sys/class/hwmon/hwmon3/pwm1'
        fan_speed_max=255
        battery='/sys/class/power_supply/BAT0/capacity'
        battery_status='/sys/class/power_supply/BAT0/status'
#Add your own hostname here, use this template:
#(edit feilds with '*' symbol and remove comments (#))
#elif hostname=='*hostname*':
#    class config:
#        hostname = ptlib.shell('uname -a').split(' ')[1]
#        cpu_temp='*path to cpu temperature*'
#        fan_speed=(*True or False (if you have a fan or not)*, '*path to fan speed (if fan is existent)*')
#        fan_speed_max=*max fan speed, 255 should work*
#        battery='*path to battery*'
#        battery_status='*path to battery status*'
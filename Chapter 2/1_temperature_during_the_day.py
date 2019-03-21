"""
How Does the Temperature Vary During the Day?
"""


from pylab import title, xlabel, ylabel, axis, plot, legend, show, savefig
from os.path import expanduser

title('FL Weather: 2/15/19 3:45pm')
xlabel('Time')
ylabel('Temperature')

times = ['4PM', '7PM', '10PM', '1AM', '4AM', '7AM', '10AM', '1PM ', '']
clearwater_temps = [69, 65, 61, 59, 59, 60, 65, 73, 73]
orlando_temps = [78, 73, 66, 63, 59, 57, 62, 74, 77]

axis(ymax=95)
axis(ymin=20)

plot(times, clearwater_temps, times, orlando_temps)
legend(['Clearwater', 'Orlando'])

# show()

savefig(expanduser('~') + '/Desktop/weather.png')

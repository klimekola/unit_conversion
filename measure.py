### Zamiana jednostek 
m = float(input('Podaj długość w metrach: '))
#1m = 100cm 1cm = 0.01m 1cal = 2.54cm = 0.0254 m, 1m=1/0.0254
mc=round(m*1/0.0254 , 2)
print(m, 'metrów to', mc ,'cali')

#stopa na cal, cal = 1/12 stopy
cs = round(mc*1/12, 2)

print(mc, 'cali to', cs, 'stóp')

sj = round(1/3*cs , 2)
print(cs, 'stóp to', sj, 'jardów')

jm = round(1/1760 * sj, 2)
print(sj, 'jardów to', jm, 'mili')

### Zamiana temperatury
c= float(input('Podaj temperature w stopniach Celsiusa: '))
F = 9/5 *c + 32
print(c, 'stopni Celsiusa to ', F , 'stopni Fahrenheita.')

f = float(input('Podaj temperature w Fahrenheitach: '))
C = -32 * 5/9 + f*5/9 
print(f, 'stopni Fahrenheita to ', C, 'stopni Celsiusa')

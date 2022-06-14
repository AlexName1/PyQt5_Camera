drone = float(input('Введите модель беспилотного воздушного средства-носителя по номеру классификатора. '
                    'Поддерживаемые в данной версии программы (1.02) модели БВС: DJI Phantom Advanced = 1, '
                    'DJI Mavic Pro = 2'))

if drone <= 1:

    carelemsizeforward = float(0.00261)

    carelemsizebroad = float(0.00261)

    carfocus = float(8.8)

    carmatrixsizefullpixforward = float(3648)

    carmatrixsizefullpixbroad = float(4864)

else:

    print('БВС нет в базе!')

camera = float(input(
    'Введите модель внешней камеры, устанавливаемой на носитель по номеру классификатора. Поддерживаемые в данной '
    'версии программы (1.02) модели: Mapir Survey 3 W RGN = 1 , Mapir Survey 3 N RGN = 2'))

if camera <= 1:

    mouelemsizeforward = float(0.00155)

    mouelemsizebroad = float(0.00155)

    moufocus = float(3.37)

    moumatrixsizefullpixforward = float(3000)

    moumatrixsizefullpixbroad = float(4000)

else:

    print('Камеры нет в базе!')

gsdprj = float(input(
    'Введите проектное GSD съемочных материалов, которое предполагается получить в результате эксплуатации внешней '
    'камеры в см/пикс'))

prodprj = float(
    input('Введите проектное продольное перекрытие для аэрофотосъемки с использованием внешней камеры в процентах'))

popprj = float(
    input('Введите проектное поперечное перекрытие для аэрофотосъемки с использованием внешней камеры в процентах'))

isoprj = float(input('Введите установленное в настройках внешней камеры ISO в единицах'))

shuprj = float(input('Введите установленную в настройках внешней камеры в секундах'))

intprj = float(input('Введите предполагаемую интервал съемки в настройках внешней камеры секундах'))

mourealsizeforward = float(mouelemsizeforward * (moumatrixsizefullpixforward))

mourealsizebroad = float(mouelemsizebroad * (moumatrixsizefullpixbroad))

Htrue = float(((gsdprj * float(10)) * moufocus) / mouelemsizeforward)

mouprojectionrealforward = float((mourealsizeforward * Htrue) / moufocus)

mouprojectionrealbroad = float((mourealsizebroad * Htrue) / moufocus)

moubasisforward = float((mouprojectionrealforward / float(100)) * ((float(100) - prodprj)))

moubasisbroad = float((mouprojectionrealbroad / float(100)) * ((float(100) - popprj)))

carrealsizeforward = float(carelemsizeforward * carmatrixsizefullpixforward)

carrealsizebroad = float(carelemsizebroad * carmatrixsizefullpixbroad)

gsdcar = float((Htrue / carfocus) * carelemsizeforward)

carprojectionrealforward = float((carrealsizeforward * Htrue) / carfocus)

carprojectionrealbroad = float((carrealsizebroad * Htrue) / carfocus)

prodolperekreal = float(((carprojectionrealforward - moubasisforward) / carprojectionrealforward) * float(100))

popperekreal = float(((carprojectionrealbroad - moubasisbroad) / carprojectionrealbroad) * float(100))

Hf = float(Htrue / 1000)

H = round(Hf)

Pdist = float(gsdprj * 0.8)

PSpeed = float((Pdist / (1 / shuprj)) / 100)

Speed = round(PSpeed)

P05real = float(((mouprojectionrealforward / 1000) - (Speed) * intprj) / ((mouprojectionrealforward / 1000)) * 100)

P05 = round(P05real)

print('Реальное продольное перекрытие съемочных материалов с внешней камеры с заданным интервалом в процентах =', P05)

print('Высота полета БАС, устанавливаемая для камеры носителя, в метрах =', H)

print('Предельная скорость полета носителя в метрах =', Speed)

Prod = round(prodolperekreal)

print(
    'Продольное перекрытие, устанавливаемое для камеры носителя в процессе формирования полетного задания в процентах, в процентах =',
    Prod)

Pop = round(popperekreal)

print(
    'Поперечное перекрытие, устанавливаемое для камеры носителя в процессе формирования полетного задания, '
    'в процентах =',
    Pop)

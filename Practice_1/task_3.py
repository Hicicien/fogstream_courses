Задание №3. В некоторой школе занятия начинаются в 9:00. Продолжительность
урока - 45 минут. После 1-го, 3-го, 5-го и т.д. уроков перемена 5 минут, а
после 2-го, 4-го, 6-го и т.д. перемена 15 минут. Дан номер урока (число от
1 до 10). Определите, когда закончится указанный урок. Выведите два целых
числа: время окончания урока в часах и минутах.
'''
 
LESSON_DURATION = 45
SHOT_BREAK = 5
LONG_BREAK = 15
START_OF_LESSONS = 540 # 9:00 в минутах 9*60=540 минут
MINUTES_IN_HOUR = 60
 
lesson_number = int(input('Введите количество уроков '))
end_of_lessons = (
    START_OF_LESSONS +
    lesson_number * LESSON_DURATION +
    SHOT_BREAK * (lesson_number//2) +
    LONG_BREAK * ((lesson_number-1)//2)
    )
hour, minutes = divmod(end_of_lessons,MINUTES_IN_HOUR)
print(f'Время окончания {lesson_number} урока {hour}:{minutes}')

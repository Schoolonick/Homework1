from math import ceil

width, height, wasted, V, percent = [float(input()) for n in range(5)]  # 10.2, 8.6, 5, 3, 20
S = round(width * height, 2)

cnt_clr_in_jar = S / wasted * 1.2  # Количество использованной краски.
cnt_jar = ceil(cnt_clr_in_jar / V)  # Количество литров в банке с учетом запаса(+1). ==7.017600000000001==
###########
cnt_not_clr_in_jar = round((cnt_jar * V) - cnt_clr_in_jar,
                           2)  # Общее количество литров в 8 банках краски, разница кол-во использованной.
###########

print(f"{S}\n"
      f"{round(cnt_clr_in_jar, 2)}\n"
      f"{cnt_jar}\n"
      f"{cnt_not_clr_in_jar}")

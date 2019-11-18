def movingAvg(array_list, numvals_for_average, size_of_array, position):
    sumvals = 0
    for i in range(numvals_for_average):
       if (position - i >= 0):
          sumvals = sumvals + array_list[position - i]
       else:
          sumvals = sumvals + array_list[size_of_array + (position - i)]
    return sumvals/numvals_for_average

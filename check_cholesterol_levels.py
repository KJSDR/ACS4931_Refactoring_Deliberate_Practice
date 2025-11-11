# By Kami Bigdely
# Decompose conditional
# Reference: https://www.healthline.com/health/high-cholesterol/levels-by-age

# Blood test analysis program

def has_good_cholesterol_level(total_cholesterol, ldl, triglyceride):
    return total_cholesterol < 200 and ldl < 100 and triglyceride < 150

def has_high_cholesterol_level(total_cholesterol, ldl, triglyceride):
    return total_cholesterol > 240 or ldl > 160 or triglyceride >= 200

def has_borderline_cholesterol_level(total_cholesterol, ldl, triglyceride):
    return (200 < total_cholesterol < 240 or 
            130 < ldl < 160 or 
            150 <= triglyceride < 200)

def report_good_level():
    print('*** Good level of cholesterol ***')

def report_high_level():
    print('*** High cholesterol level ***')
    print('start taking pills such as statins')
    print('start TLC diet')

def report_borderline_level():
    print('*** Borderline to moderately elevated ***')
    print("Start TLC diet")
    print("Under this meal plan, only 7 percent of your daily calories \nshould come from saturated fat.")
    print('Some foods help your digestive tract absorb less cholesterol. For example,\nyour doctor may encourage you to eat more:')
    print('oats, barley, and other whole grains.')
    print('fruits such as apples, pears, bananas, and oranges.')

total_cholesterol = 70
ldl = 30
triglyceride = 120

if has_good_cholesterol_level(total_cholesterol, ldl, triglyceride):
    report_good_level()
elif has_high_cholesterol_level(total_cholesterol, ldl, triglyceride):
    report_high_level()
elif has_borderline_cholesterol_level(total_cholesterol, ldl, triglyceride):
    report_borderline_level()
else:
    print('Error: unhandled case.')
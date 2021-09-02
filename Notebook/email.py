


students_email = [
                'nenavathpraveen10@gmail.com',
                'sapna98saini@gmail.com',
                '90.preeti@gmail.com',
                'aryali012@gmail.com',
                'venkateshmamidala39@gmail.com',
                'somasekhardesigns@gmail.com',   
                'zeddkhan101@gmail.com',
                'kumarkartavay@gmail.com',
                'biswajit27m@gmail.com',
                'sp4185202@gmail.com',
                'neerajpal8548@gmail.com',
                'sbankar217@gmail.com',
                'cp150496@gmail.com',
                'santprakash28877@gmail.com',
                'vgowdavenu112@gmail.com',
                'scorpioveer@gmail.com',
                'veershinde195@gmail.com',
                'safikulsk732@gmail.com',
                '90.preeti@gmail.com',
                'sapna98saini@gmail.com',
                'bhavanreddy326@gmail.com',
                'khanabdulgani_87@yahoo.com',
                'kumarkartavay@gmail.com',
                'bariavs41@gmail.com',
                'somasekhardesigns@gmail.com',
                'saurabhdongre16@gmail.com',
                'saurabhdongre16@gmail.com',
                'zeddkhan101@gmail.com',
                'zeddkhan101@gmail.com',
                'kumarkartavay@gmail.com',
                'kumarkartavay@gmail.com',
                'parthivbhatti007@gmail.com',
                'bhattiujjval007@gmail.com',
                'kumarkartavay@gmail.com',
                'kumarkartavay@gmail.com',
                'santprakash28877@gmail.com',
                'rajnishkumar8595@gmail.com',
                's.kumar.s8101997@gmail.com ',
                'kanhu.kcn@gmail.com',
                'zeddkhan101@gmail.com',
                'govindsarraf4109@gmail.com',
                'himanshugoyal785@gmail.com',
                'bhattiujjval007@gmail.com',
                'shailendermy.10@gmail.com' ,
                'saurabhdongre16@gmail.com',
                'nitypatel6@gmail.com',
                'subirsgghosh@gmail.com',
                'jk426704@gmail.com',
                'gokulharsha06@gmail.com',
                'parthivbhatti007@gmail.com',
                'nm.mahesh66@gmail.com',
                'bariavs41@gmail.com',
                'amarsharma00786@gmail.com',
                'sharmadheeraj849@gmail.com ',
                'santprakash28877@gmail.com',
                'ruthvikchintam@gmail.com',
                'bhavanreddy326@gmail.com',
                'bariavs41@gmail.com'
            
            ]
temp = [

        

]
no_of_students = len(students_email)
# print(no_of_students)

# remove duplicate 
students_email =list(set(students_email))
# sorted list
students_email.sort()
# print(len(students_email))
# print students mail serially
for student in range(len(students_email)):
    print(str((student+1)).rjust(2,' '), students_email[student])
    # print(students_email[student],',')

# temp2 = []
# for i in temp:
#     if i not in students_email:
#         temp2.append(i)
# for i in temp2:
#     print(i,',')
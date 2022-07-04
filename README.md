1. video when web is running automate
https://user-images.githubusercontent.com/62136934/177195998-d0c03d89-d594-47ae-b47f-c2257f537bf1.mp4


2. Database
```
SELECT student.name, class.name
FROM student
JOIN student_class ON student.id = student_class.student_id
JOIN class ON class.id = student_class.course_id;
```

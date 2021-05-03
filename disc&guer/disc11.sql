select Name from records where Supervisor="Oliver Warbucks";

select * from records where Name=Supervisor;

select Name from records where Salary>50000 order by Name;

select Day,Time from records as r,meetings as m where r.Division=m.Division and Supervisor="Oliver Warbucks";

select r1.Name from records as r1,records as r2 where r1.Supervisor=r2.Name and r1.Division!=r2.Division;

select r1.Name,r2.Name from records as r1,records as r2,meetings as m1,meetings as m2 where r1.Division=m1.Division and r2.Division=m2.Division and m1.Day=m2.Day and m1.Time=m2.Time and r1.Name<r2.Name;

select Supervisor,sum(Salary) from records group by Supervisor;

select Day from records as r,meetings as m where r.Division=m.Division group by Day having count(*)<5;

select e1.divison from records as e1,records as e2 where e1.name!=e2.name and e1.division=e2.division group by e1.divison having max(e1.salary+e2.salary)<100000;

create table num_taught as
    select professor as professor,course as course,count(*) as times from courses group by professor,course;

select t1.professor,t2.professor,t1.course from num_taught as t1,num_taught as t2 where t1.course=t2.course and t1.times=t2.times and t1.professor<t2.professor;

select a.professor,b.professor from num_taught as a,num_taught as b where a.course=b.course and a.semester=b.semester and a.professor<b.professor group by a.professor,b.professor,a.course having count(*)>1;
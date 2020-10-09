from collections import namedtuple
from typing import List

class schedulling:
    def __init__(self, jobs: List[int]) -> None:
        """
        assign jobs as istance of class schedulling
        """
        self.jobs = jobs

    def shedule(self, totalJobs:int, deadline:List[int]) -> List[int]:
        """
        Parameteres  : total_jobs  and list of deadline of jobs
        Returns : List of jobs_id which are profitable  and can be done before
                  deadline
        >>> a = Scheduling([(0, 13, 10),(1, 2, 20),(2, 33, 30),(3, 16, 40)])
        >>> a.schedule( 3, [3, 4, 5])
        [(1, 2, 20), (2, 33, 30)]
        >>> a = Scheduling([(0, 13, 10),(1, 2, 20),(2, 33, 30),(3, 16, 40)])
        >>> a.schedule( 4, [13, 2, 33, 16])
        [(1, 2, 20), (2, 33, 30), (3, 16, 40)]
        """
        self.j = [self.jobs[1]]
        self.x = 2
        while self.x < totalJobs:
            self.k = self.j.copy()
            self.k.append(self.jobs[self.x])
            self.x += 1
            if self.feasible(self.k, deadline):
                self.j = self.k.copy()

        return self.j

    def feasible(self, profitJobs:List[int], deadline:List[int]) -> bool:
        """
        Parameters : list of current profitable jobs within deadline
                     list of deadline of jobs
        Returns : true if k[-1] job is profitable to us else false
        >>> a = Scheduling([(0, 13, 10),(1, 2, 20),(2, 33, 30),(3, 16, 40)])
        >>> a.feasible( [0], [2, 13, 16, 33] )
        True
        >>> a = Scheduling([(0, 13, 10),(1, 2, 20),(2, 33, 30),(3, 16, 40)])
        >>> a.feasible([0], [2, 13, 16, 33] )
        True
        """

        self.tmp = profitJobs
        self.isFeasible = True
        
        i = 0
        j = 1
        k = 0

        while i < len(self.tmp):
            while j < len(self.tmp):
                self.index1 = self.jobs.index(self.tmp[i])
                self.index2 = self.jobs.index(self.tmp[j])
                j += 1
                if deadline[self.index1] > deadline[self.index2]:
                    (self.tmp[i], self.tmp[j]) = (
                        self.tmp[j],
                        self.tmp[i],
                    )
            i += 1

        while k < len(self.tmp):
            self.job = self.tmp[k]
            if self.job in self.jobs:
                self.jobIndex = self.jobs.index(self.job)
            else:
                self.jobInde = 0
            self.dlineval = deadline[self.jobIndex]
            self.ftest = k + 1
            k += 1
            if self.dlineval < self.ftest:
                self.isFeasible = False
                break

        return self.isFeasible

def main():
    job = namedtuple("job","job_id is deadline profit")
    jobs = [
        job(0, 0, 0),
        job(1, 2, 46),
        job(2, 4, 52),
        job(3, 3, 30),
        job(4, 3, 36),
        job(5, 2, 56),
        job(6, 1, 40),
    ]

    midResult = []
    for i in range(len(jobs)):
        currentJob = []
        currentJob.extend((jobs[i].deadline, jobs[i].profit, jobs[i].job_id))
        midResult.append(currentJob)
    midResult.sort(key=lambda k: (k[0],-k[1]))
    (deadline, profit, jobs) = map(list, zip(*midResult))
    
    schedullingJobs = schedulling(jobs)
    scheduledJobs = schedullingJobs.schedule(len(jobs), deadline)
    print(f"\n jobs{scheduledJobs}")
    
    finalProfit = []
    finaldl = []

    for i, item in enumerate(scheduledJobs):
        jobsindex = jobs.index(item)
        finalProfit.append(profit[jobsindex])
        finaldl.append(deadline[jobsindex])

    print(f"\n profit {finalProfit}")
    print(f"\n deadline {finaldl}")


if __name__== "__main__":
    main()
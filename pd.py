class IPrisonerDilemnaAlgorithm:
    """Interface for implementing a Prisoner Dilemna optimization algorithm"""
    def __init__(self):
        a = 1
    def perform(self, enemy_cooperated):
        return True
    
class JesusAlgorithm(IPrisonerDilemnaAlgorithm):
    """Always cooperate"""
    def perform(self, enemy_cooperated):
        return True

class LuciferAlgorithm(IPrisonerDilemnaAlgorithm):
    """Always cheat"""
    def perform(self, enemy_cooperated):
        return False

class SmartAlgorithm(IPrisonerDilemnaAlgorithm):
    """Do what other does"""
    def perform(self, enemy_cooperated):
        if enemy_cooperated is not False and enemy_cooperated is not True:
            return True
        return enemy_cooperated

class LenientSmartAlgorithm(IPrisonerDilemnaAlgorithm):
    """Do what other does with 10% to default to cooperate"""
    def perform(self, enemy_cooperated):
        if enemy_cooperated is not False and enemy_cooperated is not True:
            return True
        if random.randint(0,10) is 0:
            return True
        return enemy_cooperated
    
def compete(algorithm1, algorithm2, iterations=1000):
    cooperate_success_pt = 100
    defect_success_pt = 100
    cooperate_fail_pt = 10
    defect_fail_pt = 30
    algo1_s = 0
    algo2_s = 0
    algo1_l = 0
    algo2_l = 0
    for i in range(iterations):
        algo1_l = algorithm1.perform(algo2_l)
        algo2_l = algorithm2.perform(algo1_l)
        if algo1_l is algo2_l and algo1_l is True:
            print("Double cooperate")
            algo1_s += cooperate_success_pt
            algo2_s += cooperate_success_pt
        elif algo1_l is algo2_l and algo1_l is False:
            print("Double defect")
            algo1_s += defect_fail_pt
            algo2_s += defect_fail_pt
        elif algo1_l is False:
            print("Algorithm1 successful defect")
            algo1_s += defect_success_pt
            algo2_s += cooperate_fail_pt
        else:
            print("Algorithm2 successful defect")
            algo1_s += cooperate_fail_pt
            algo2_s += defect_success_pt
    print("Final result: \nAlgorithm1: ", algo1_s,"\nAlgorithm2: ", algo2_s)

compete(SmartAlgorithm(), SmartAlgorithm())
compete(JesusAlgorithm(), LuciferAlgorithm())

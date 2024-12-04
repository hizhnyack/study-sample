from self_howitworks import human, jane

ann = human('Ann', 28,'female')
igor = human('Igor', 56,'male')

ann.speak()
# Igor.speak()
jane.speak()

ann.chage(jane)

ann.speak()
# Igor.speak()
jane.speak()


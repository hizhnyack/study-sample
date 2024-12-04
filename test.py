from self_howitworks import human, Jane

Ann = human(28,'female')
Igor = human(56,'male')

Ann.speak()
# Igor.speak()
Jane.speak()

Ann.change(Jane)

Ann.speak()
# Igor.speak()
Jane.speak()


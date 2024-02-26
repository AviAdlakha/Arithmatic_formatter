def arithmetic_arranger(problems, val=False):

  toprow = ''
  bottomrow = ''
  dashrow = ''
  solutionrow = ''
  solution = ''
  op = ''
  first = 1
  if len(problems) > 5:
    return "Error: Too many problems."
  for problem in problems:

    dummy = problem
    problem = problem.split()
    op = problem[1]
    if op not in {'+', '-'}:
      return "Error: Operator must be '+' or '-'."
    if len(problem[0]) > 4 or len(problem[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
    try:
      problem[0] = int(problem[0])
      problem[2] = int(problem[2])
    except:
      return "Error: Numbers must only contain digits."
    solution = (eval(dummy))
    if first != 1:
      toprow += "    "
      bottomrow += "    "
      dashrow += "    "
      solutionrow += "    "
    first = 0

    width = max(len(str(problem[0])), len(str(problem[2]))) + 1

    toprow += str(problem[0]).rjust(width + 1)
    bottomrow += op
    bottomrow += str(problem[2]).rjust(width)
    dashrow += str((width + 1) * '-')
    solutionrow += str(solution).rjust(width + 1)

  if val:
    arranged_problems = '\n'.join((toprow, bottomrow, dashrow, solutionrow))
  else:
    arranged_problems = '\n'.join((toprow, bottomrow, dashrow))

  return arranged_problems

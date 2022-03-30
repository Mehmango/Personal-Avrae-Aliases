embed
<drac2>
g, n, c = '&1&', &ARGS&[1:], combat()
if c:
  cmbts = [c.get_combatant(x) for x in n if c.get_combatant(x)]
  [x.set_group(g) for x in cmbts]
  names= '\n'.join([x.name for x in cmbts])
  return f""" -desc "Combatants added to group {g}: \n{names}" """
</drac2>
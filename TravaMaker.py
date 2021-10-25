class Trava():
  def zigzag(File, *Text):
    with open(File, "w") as TravaWrite:
      TravaWrite.write(f"""
{Text}
 {Text}
  {Text}
   {Text}
    {Text}
     {Text}
      {Text}
       {Text}
        {Text}
         {Text}
          {Text}
         {Text}
        {Text}
       {Text}
      {Text}
     {Text}
    {Text}
   {Text}
  {Text}
 {Text}
{Text}
""")

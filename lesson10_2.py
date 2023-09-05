{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "=====取名字系統========\n",
      "\n",
      "\n",
      "張貞妃\n",
      "張致恬\n",
      "張淑婷\n",
      "張偉成\n",
      "張傑宣\n",
      "張振瑋\n",
      "張麗卿\n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "invalid literal for int() with base 10: ''",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[4], line 15\u001b[0m\n\u001b[1;32m     13\u001b[0m names_list \u001b[39m=\u001b[39m allNames()\n\u001b[1;32m     14\u001b[0m first_name \u001b[39m=\u001b[39m \u001b[39minput\u001b[39m(\u001b[39m\"\u001b[39m\u001b[39m請輸入您的姓:\u001b[39m\u001b[39m\"\u001b[39m)\n\u001b[0;32m---> 15\u001b[0m count \u001b[39m=\u001b[39m \u001b[39mint\u001b[39;49m(\u001b[39minput\u001b[39;49m(\u001b[39m\"\u001b[39;49m\u001b[39m請輸入您要的筆數:\u001b[39;49m\u001b[39m\"\u001b[39;49m))\n\u001b[1;32m     16\u001b[0m random_names \u001b[39m=\u001b[39m random\u001b[39m.\u001b[39mchoices(names_list,k\u001b[39m=\u001b[39mcount)\n\u001b[1;32m     17\u001b[0m \u001b[39mfor\u001b[39;00m name \u001b[39min\u001b[39;00m random_names:\n",
      "\u001b[0;31mValueError\u001b[0m: invalid literal for int() with base 10: ''"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "def allNames() -> list:\n",
    "    names_list = []\n",
    "    with open(\"names.txt\",encoding=\"utf-8\") as file:    \n",
    "        for line in file:\n",
    "            names_list.append(line[:3])\n",
    "    return names_list\n",
    "\n",
    "print(\"=====取名字系統========\\n\\n\")\n",
    "\n",
    "while(True):\n",
    "    names_list = allNames()\n",
    "    first_name = input(\"請輸入您的姓:\")\n",
    "    count = int(input(\"請輸入您要的筆數:\"))\n",
    "    random_names = random.choices(names_list,k=count)\n",
    "    for name in random_names:\n",
    "        print(first_name + name[-2:])\n",
    "    \n",
    "    again = input(\"您還要繼續嗎?(y,n)\")\n",
    "    if again.lower() == \"n\":\n",
    "        break\n",
    "\n",
    "print(\"系統結束\")\n",
    "    "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.12"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

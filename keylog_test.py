#python test file

import pythoncom, pyHook

def OnMouseEvent(event):
	print('MessageName: ',event.MessageName)
	print('Message: ', event.Message)
	print('Time: ', event.Time)
	print('Window: ',event.Window)
	print('WindowName: ', event.WindowName)
	print('Position: ',event.Position)
	print('Wheel: ', event.Wheel)
	print('Injected: ',event.Injected)
	print('----')
	

hm=pyHook.HookManager()

hm.MouseAll=OnMouseEvent

hm.HookMouse()

pythoncom.PumpMessages()	
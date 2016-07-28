#ListCreate Plugin
#Click nodes & run Script
#Based On Selection

import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Windows')
clr.AddReference('DynamoCore')
clr.AddReference('DynamoCoreWpf')
import System.Windows.Forms as WinForms
from System.Collections.Generic import IEnumerable, List
from Dynamo.Graph.Nodes import *
from System.Guid import NewGuid, ToByteArray
from Dynamo.Models import *
#from System.Collections.Generic import List
#from Dynamo.Wpf.ViewModels.Watch3D import *

def maxXPos(selectedNodes):
    maxX = 0
    for item in selectedNodes:
        if item.X+item.Width > maxX:
            maxX = item.X +item.Width
    return maxX

def avgY (selectedNodes):
    sumY = 0
    for item in selectedNodes:
        sumY+=item.Y;
    return (sumY/len(selectedNodes))


#nodeId = NewGuid()
selectedNodes = List[NodeModel](workspaceModel.CurrentSelection)
#commandExecutive.ExecuteCommand(DynamoModel.CreateNodeCommand(nodeId.ToString(),"List.Create",maxXPos(selectedNodes)+50,avgY(selectedNodes),False,False),None,None)
count = 0
for item in selectedNodes[0].OutPorts:
    commandExecutive.ExecuteCommand(DynamoModel.MakeConnectionCommand(selectedNodes[0].GUID,count,PortType.Output,DynamoModel.MakeConnectionCommand.Mode.Begin),None,None)
    commandExecutive.ExecuteCommand(DynamoModel.MakeConnectionCommand(selectedNodes[1].GUID,count,PortType.Input,DynamoModel.MakeConnectionCommand.Mode.End),None,None)
    count+=1
    
#var pointOriginNo 	de = new DSFunction(CurrentDynamoModel.LibraryServices.GetFunctionDescriptor("Point.Origin"));
#nodeId = Guid]()
#nodeId.add(NewGuid());


#sortedNodes = sorted(selectedNodes,key=attrgetter('Y'))
#watch3DViewModel.SetCameraData(CameraData())
#w.SetCameraData(

#enumerator = IEnumerable[NodeModel].GetEnumerator(workspaceModel.CurrentSelection);
#for x in enumerator: 

#WinForms.MessageBox.Show(str(maxXPos(selectedNodes)), 'hello')
#WinForms.MessageBox.Show(str(selectedNodes[0].Width), 'hello')
#WinForms.MessageBox.Show(str(selectedNodes[0].X), 'hello')
#WinForms.MessageBox.Show(str(selectedNodes[0].Y), 'hello')
#WinForms.MessageBox.Show(str(selectedNodes[0].Height), 'hello')

#s = List[](workspaceModel.CurrentSelection) 
#for x in s: WinForms.MessageBox.Show(x.CreationName, 'hello')
#WinForms.MessageBox.Show(workspaceModel.FileName, 'hello')

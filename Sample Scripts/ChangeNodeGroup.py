#ChangeNodeGroup Script
#Click on nodes to move to another group & select destination group 
#Run Script
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
from Dynamo.Wpf.ViewModels.Watch3D import *

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

def changeNodeGroup(selectedNodes):
	for item in selectedNodes:
		commandExecutive.ExecuteCommand(DynamoModel.UngroupModelCommand(item.GUID),None,None)
		commandExecutive.ExecuteCommand(DynamoModel.AddModelToGroupCommand(item.GUID),None,None)
    
selectedNodes = List[NodeModel](workspaceModel.CurrentSelection)
changeNodeGroup(selectedNodes)
#commandExecutive.ExecuteCommand(DynamoModel.UngroupModelCommand(selectedNodes[0].GUID),None,None)
#commandExecutive.ExecuteCommand(DynamoModel.AddModelToGroupCommand(selectedNodes[0].GUID),None,None)


#var pointOriginNo 	de = new DSFunction(CurrentDynamoModel.LibraryServices.GetFunctionDescriptor("Point.Origin"));
#nodeId = Guid]()
#nodeId = NewGuid();
#nodeId.add(NewGuid());

#watch3DViewModel.SetCameraData(CameraData())
#w.SetCameraData(

#enumerator = IEnumerable[NodeModel].GetEnumerator(workspaceModel.CurrentSelection);
#for x in enumerator: 
#dynamoViewModel.ExecuteCommand(DynamoModel.CreateNodeCommand(nodeId.ToString(),"List.Create",maxXPos(selectedNodes)+50,avgY(selectedNodes),False,False),None,None)
#count = 0;
#for item in selectedNodes:
 #   dynamoViewModel.ExecuteCommand(DynamoModel.ModelEventCommand(nodeId.ToString(),"AddInPort"),None,None)
  #  dynamoViewModel.ExecuteCommand(DynamoModel.MakeConnectionCommand(item.GUID,0,PortType.Output,DynamoModel.MakeConnectionCommand.Mode.Begin),None,None)
   # dynamoViewModel.ExecuteCommand(DynamoModel.MakeConnectionCommand(nodeId,count,PortType.Input,DynamoModel.MakeConnectionCommand.Mode.End),None,None)
   # count+=1
#WinForms.MessageBox.Show(str(maxXPos(selectedNodes)), 'hello')
#WinForms.MessageBox.Show(str(selectedNodes[0].Width), 'hello')
#WinForms.MessageBox.Show(str(selectedNodes[0].X), 'hello')
#WinForms.MessageBox.Show(str(selectedNodes[0].Y), 'hello')
#WinForms.MessageBox.Show(str(selectedNodes[0].Height), 'hello')

#s = List[](workspaceModel.CurrentSelection) 
#for x in s: WinForms.MessageBox.Show(x.CreationName, 'hello')
#WinForms.MessageBox.Show(workspaceModel.FileName, 'hello')

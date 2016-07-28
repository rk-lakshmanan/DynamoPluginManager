#Camera Top 


import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Windows')
clr.AddReference('DynamoCore')
clr.AddReference('DynamoCoreWpf')
clr.AddReference('WindowsBase')
clr.AddReference('DynamoUtilities')
clr.AddReference('PresentationCore')
import System.Windows.Forms as WinForms
from System.Collections.Generic import IEnumerable, List
from Dynamo.Graph.Nodes import *
from System.Guid import NewGuid, ToByteArray
from Dynamo.Models import *
from Dynamo.Graph.Connectors import *
from Dynamo.Graph.Workspaces import *
from System.Windows import *
from Dynamo.Utilities import *
from Dynamo.Selection import *
#from System.Collections.Generic import List
from Dynamo.Wpf.ViewModels.Watch3D import *
from System.Windows.Media.Media3D import *


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
def log(floatValue):
    Logger.Log(str(floatValue))
def logs(stringVal,floatValue):
    Logger.Log(stringVal+" "+str(floatValue))

#watch3DViewModel.SetCameraData(CameraData())
d = watch3DViewModel.GetCameraInformation()
newD = CameraData()
newD.EyePosition = Point3D(-5.14,73.08,3.64)
newD.UpDirection = Vector3D(0.0110,0.39073,-0.9204)
newD.LookDirection = Vector3D(0.14,-62,-11)
newD.NearPlaneDistance = 0.10000000149
newD.FarPlaneDistance = 163.676940918
logs("eyePosX",d.EyePosition.X)
logs("eyePosY",d.EyePosition.Y)
logs("eyePosZ",d.EyePosition.Z)
logs("UpDirectX",d.UpDirection.X)
logs("UpDirectY",d.UpDirection.Y)
logs("UpDirectZ",d.UpDirection.Z)
logs("LookDirX",d.LookDirection.X)
logs("LookDirY",d.LookDirection.Y)
logs("LookDirZ",d.LookDirection.Z)
logs("nearPlaneDist",d.NearPlaneDistance)
logs("farPlaneDistance",d.FarPlaneDistance)
watch3DViewModel.SetCameraData(newD)




#nodeId = NewGuid()
#selectedNodes = List[NodeModel](workspaceModel.CurrentSelection)
#commandExecutive.ExecuteCommand(DynamoModel.CreateNodeCommand(nodeId.ToString(),"List.Create",maxXPos(selectedNodes)+50,avgY(selectedNodes),False,False),None,None)
#count = 0
#for item in selectedNodes:
 #   if(count < len(selectedNodes)-1):
 #       commandExecutive.ExecuteCommand(DynamoModel.ModelEventCommand(nodeId.ToString(),"AddInPort"),None,None)
 #   commandExecutive.ExecuteCommand(DynamoModel.MakeConnectionCommand(item.GUID,0,PortType.Output,DynamoModel.MakeConnectionCommand.Mode.Begin),None,None)
 #   commandExecutive.ExecuteCommand(DynamoModel.MakeConnectionCommand(nodeId,count,PortType.Input,DynamoModel.MakeConnectionCommand.Mode.End),None,None)
 #   count+=1
    
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

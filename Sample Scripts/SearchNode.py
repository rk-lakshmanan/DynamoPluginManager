#Search Node
#Select AND Search
#clr.AddReference('System.Windows.Forms') 
#import System.Windows.Forms as WinForms 
#WinForms.MessageBox.Show('Hello', 'Hello World')

import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System')
clr.AddReference('System.Windows')
clr.AddReference('DynamoCore')
clr.AddReference('DynamoCoreWpf')
clr.AddReference('WindowsBase')
clr.AddReference('DynamoUtilities')
#clr.AddReference('System.Drawing')
#from System.Drawing import Point
from System.Windows.Forms import *
from System.Collections.Generic import IEnumerable, List
from Dynamo.Graph.Nodes import *
from System.Guid import NewGuid, ToByteArray
from Dynamo.Models import *
from Dynamo.Graph.Connectors import *
from Dynamo.Graph.Workspaces import *
from System.Windows import *
from Dynamo.Utilities import *
from Dynamo.Selection import *
from System.Collections import ArrayList
from System.Diagnostics import *


resultNodes = List[NodeModel]()
#from System.Collections.Generic import List
array = ArrayList
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


def cameraFindAndFocusOnSelectedNode():
    zoomBorder = workspaceView.FindName("zoomBorder")
    if zoomBorder == None:
        Logger.Log("failed")    
    outerCanvas = workspaceView.FindName("outerCanvas")
    if outerCanvas == None:
        Logger.Log("Canvas failed")
    
    minX = workspaceViewModel.GetSelectionMinX();
    logs("minX",minX)
    minY = workspaceViewModel.GetSelectionMinY();
    logs("minY",minY)
    maxX = workspaceViewModel.GetSelectionMaxX();
    logs("maxX",maxX)
    maxY = workspaceViewModel.GetSelectionMaxY();
    logs("maxY",maxY)
    offset = Point2D(minX,minY)
    logs("offset",offset)
    focusWidth = maxX - minX;
    logs("focusWidth",focusWidth)
    focusHeight = maxY - minY;
    logs("focusWidth",focusHeight)

    viewPortPadding = 30

    fitWidth = outerCanvas.ActualWidth - 2 *viewPortPadding
    fitHeight = outerCanvas.ActualHeight - 2 *viewPortPadding
    logs("fitwidth",fitWidth)
    logs("fitHeignth",fitHeight)




    scaleX = fitWidth/focusWidth
    scaleY = fitHeight/focusHeight
    scaleRequired = 1

    centerOffsetX = viewPortPadding + (fitWidth - (focusWidth * scaleRequired)) / 2;
    centerOffsetY = viewPortPadding + (fitHeight - (focusHeight * scaleRequired)) / 2;

    resultOffset = Point2D(0,0)
    resultOffset.X = -(offset.X * scaleRequired) + centerOffsetX;
    resultOffset.Y = -(offset.Y * scaleRequired) + centerOffsetY;

    logs("x",resultOffset.X)
    logs("y",resultOffset.Y)


    workspaceModel.Zoom = scaleRequired
    workspaceModel.X = resultOffset.X
    workspaceModel.Y = resultOffset.Y

    zoomBorder.SetTranslateTransformOrigin(Point2D(workspaceModel.X,workspaceModel.Y))
#workspaceModel.Zoom = 5


    log(selectedNodes[0].X)
    log(selectedNodes[0].Y)

def getData(node):
    identifier = node.AstIdentifierBase
    mirror = dynamoViewModel.Model.EngineController.GetMirror(identifier)
    log(mirror)
    logs("data",mirror.GetData().Data)
    return mirror.GetData().Data    

def UpdateArray(sender,event):
    log("update")


def OnSelected(sender,event):
   # empty = NewGuid
    commandExecutive.ExecuteCommand(DynamoModel.SelectModelCommand("00000000-0000-0000-0000-000000000000",0),None,None)
    commandExecutive.ExecuteCommand(DynamoModel.SelectModelCommand(resultNodes[sender.SelectedIndex].GUID,0),None,None)
    log(sender.SelectedItem)
    cameraFindAndFocusOnSelectedNode()

###########################################################

#							CLASS 
##########################################################   
class DataBoundListBoxExample(Form):

    def __init__(self):
        self.Text = 'Data Bound ListBox Example'
        
        box = ListBox()
        box.Dock = DockStyle.Fill
        self.Controls.Add(box)
        box.SelectedIndexChanged += self.OnSelected
        
        array = ArrayList()
        for i in xrange(100):
          array.Add(i)
         
        box.DataSource = array
        
    def OnSelected(self,sender,event):
        log("hello")
        
###########################################################

#							MAIN 
##########################################################
selectedNodes = List[NodeModel](workspaceModel.CurrentSelection)
workspaceNodes = List[NodeModel](workspaceModel.Nodes)

for item in workspaceNodes:
    logs("itesmlislt",item.CreationName)
    if (item.CreationName == selectedNodes[0].CreationName):
       resultNodes.Add(item)
blank = " "
myForm = Form()
myForm.Text = 'List'
array = None       
array = ArrayList()
for item in resultNodes:
    s = "{0} {1} {2} {3}".format(item.NickName, item.X,item.Y,getData(item))
    array.Add(s)
box = ListBox()
box.Dock = DockStyle.Fill

myForm.Controls.Add(box)
box.SelectedIndexChanged += OnSelected



box.DataSource = array
myForm.Show()

#Application.Run(DataBoundListBoxExample())
#var pointOriginNo     
#nodeId = Guid]()
nodeId = NewGuid();
#nodeId.add(NewGuid());


#cameraFindAndFocusOnSelectedNode()




#v = dynamoViewModel.CurrentSpaceViewModel
#v.FitViewInternal();
#x = selectedNode[0].X
#workspaceModel.X = selectedNodes[0].X
#workspaceModel.Y = selectedNodes[0].Y
#((WorkSpaceModel) workspaceModel).OnCurrentOffsetChanged(DynamoViewModel,Point2D(workspaceModel.X+10,workspaceModel.Y+10))
#dynamoViewModel.get

#zoomBorder.SetTranslateTransformOrigin(Point2D(workspaceModel.X,workspaceModel.Y));
#workspaceViewModel.RequestZoomToFitView
#workspaceViewModel.ResetFitViewToggleCommand.Execute(false);
#Logger.Log(str(workspaceNodes[0].X))    
#vm = WorkspaceViewModel (dynamoViewModel.CurrentSpaceViewModel)
#workspaceModel.Zoom = 1    
#workspaceModel.X = workspaceModel.X+10
#workspaceModel.Y = workspaceModel.Y+10
#((WorkSpaceModel) workspaceModel).OnCurrentOffsetChanged(DynamoViewModel,Point2D(workspaceModel.X+10,workspaceModel.Y+10))
#zoomBorder.SetTranslateTransformOrigin(Point2D(workspaceModel.X+10,workspaceModel.Y+10));
#workspaceViewModel.ResetFitViewToggleCommand.Execute(false);
#Logger.Log(str(workspaceNodes[0].X))
#Logger.Log(str(workspaceViewModel.GetSelectionAverageX()))
#workspaceModel.Zoom = 5






#Item1inputPorts= List[PortModel](selectedNodes[0].InPorts)
#Item1outputPorts = List[PortModel](selectedNodes[0].OutPorts)
#Item1Connectors = List[ConnectorModel](Item1outputPorts[0].Connectors)

#for connectors in Item1Connectors:
#    tempNodeModel = connectors.End.Owner
#    portIndex = connectors.End.Index
#    dynamoViewModel.ExecuteCommand(DynamoModel.MakeConnectionCommand(selectedNodes[1].GUID,0,PortType.Output,DynamoModel.MakeConnectionCommand.Mode.Begin),None,None)
#    dynamoViewModel.ExecuteCommand(DynamoModel.MakeConnectionCommand(tempNodeModel.GUID,portIndex,PortType.Input,DynamoModel.MakeConnectionCommand.Mode.End),None,None)


#workspaceModel.X = -10000
#WinForms.MessageBox.Show(str(workspaceModel.Author), 'hello')
#WinForms.MessageBox.Show(str(workspaceModel.Y), 'hello')

#enumerator = IEnumerable[NodeModel].GetEnumerator(workspaceModel.CurrentSelection);
#for x in enumerator: 
#dynamoViewModel.ExecuteCommand(DynamoModel.CreateNodeCommand(nodeId.ToString(),"List.Create",maxXPos(selectedNodes)+50,avgY(selectedNodes),False,False),None,None)
#count = 0;
#for item in selectedNodes:
#    if(count < len(selectedNodes)-1):
 #       dynamoViewModel.ExecuteCommand(DynamoModel.ModelEventCommand(nodeId.ToString(),"AddInPort"),None,None)
  #  dynamoViewModel.ExecuteCommand(DynamoModel.MakeConnectionCommand(item.GUID,0,PortType.Output,DynamoModel.MakeConnectionCommand.Mode.Begin),None,None)
   # dynamoViewModel.ExecuteCommand(DynamoModel.MakeConnectionCommand(nodeId,count,PortType.Input,DynamoModel.MakeConnectionCommand.Mode.End),None,None)
   # count+=1
#selectedNodes[0].X +=100



#WinForms.MessageBox.Show(str(maxXPos(selectedNodes)), 'hello')
#WinForms.MessageBox.Show(str(selectedNodes[0].Width), 'hello')
#inForms.MessageBox.Show(str(selectedNodes[0].X), 'hello')
#WinForms.MessageBox.Show(str(selectedNodes[0].Y), 'hello')
#WinForms.MessageBox.Show(str(selectedNodes[0].Height), 'hello')

#s = List[](workspaceModel.CurrentSelection) 
#for x in s: WinForms.MessageBox.Show(x.CreationName, 'hello')
#WinForms.MessageBox.Show(workspaceModel.FileName, 'hello')

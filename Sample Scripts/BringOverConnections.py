#BringOverConnections brings over output port connections from first selected node to the second selected node
#Select origin node and select destination node 
#Then Run Script
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
from Dynamo.Graph.Connectors import *
#from System.Collections.Generic import List

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

nodeId = NewGuid();

selectedNodes = List[NodeModel](workspaceModel.CurrentSelection)

Item1outputPorts = List[PortModel](selectedNodes[0].OutPorts)
Item1Connectors = List[ConnectorModel](Item1outputPorts[0].Connectors)

for connectors in Item1Connectors:
	tempNodeModel = connectors.End.Owner
	portIndex = connectors.End.Index
	commandExecutive.ExecuteCommand(DynamoModel.MakeConnectionCommand(selectedNodes[1].GUID,0,PortType.Output,DynamoModel.MakeConnectionCommand.Mode.Begin),None,None)
	commandExecutive.ExecuteCommand(DynamoModel.MakeConnectionCommand(tempNodeModel.GUID,portIndex,PortType.Input,DynamoModel.MakeConnectionCommand.Mode.End),None,None)

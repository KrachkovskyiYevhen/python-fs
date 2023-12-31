python-fs
python-fs is a Python package for creating a FERAG string file programmatically. If you don't know what FERAG (the company) or a FERAG string is you probably don't need this package ;-)

The shortest possible FERAG string
According to FERAG's documentation this is the shortest possible FERAG string:

%2440+40DEMO2009!
%2401+11E1_ROUTE_100 !
%2402+11E1_ROUTE_100 +590+91000000+20E1 !
%2403+12R100RE001 +1300123!
%2406+11E1_ROUTE_100 !
%2441+40DEMO2009!
The variable values are:

the title is 'DEMO2009'
a route named 'E1_ROUTE_100'
an edition called 'E1'
a production drop 'R100RE001' with 123 copies
Usage

from feragstring import FeragString

fs = FeragString()
fs.SetTitleName("EDITION1")

# set title parameters

fs.TitleInfo.SetPrintObjectName("EDITION1A")
fs.TitleInfo.SetPublicationDate("2020-05-31")
fs.TitleInfo.SetCountryCode("13")
fs.TitleInfo.SetPrintObjectColor("00000000")

pr1 = fs.productReference.NewProductReference()
pr1.SetProductName("MAIN")
pr1.SetCopiesAssigned(25000)
pr1.SetSupervision(1)
pr1.SetOverlap(5)
mp = fs.missingParameter.NewMissingParameter(1, 1)
pr1.SetMissingParameter(mp)
pr1.SetIssueReference("MAIN01")
fs.AddProductReference(pr1)

# add a route

rt = fs.route
rt.SetRouteName("ROUTE001")
rt.SetRouteCode(fs.NextRouteCode())
rt.SetRampNumber(0)
rt.SetCopiesInRoute(1500)
rt.SetLimit(1)
rt.SetMaxStack(13)
rt.SetStandard(40)
rt.SetParameterN(4)
rt.SetMaxBundle(40)
rt.SetTopsheetMarker(5)
rt.SetEaMarker(0)
rt.SetTopsheetTemplateDirectory(20)
rt.AddProductReferenceNumber(1)
fs.AddRoute(rt)

print(fs.PrintOut())

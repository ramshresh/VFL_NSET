s=r"Awareness Raising  Education and Training (1), Climate Change Adaptation (1), Climate Change Mitigation (1), Dam/Dyke Building (6), Disaster Preparedness (2), Drainage Channels (1), Early Warning Systems (EWS) (1), Investment in Infrastructure Improvement and Mitigation Works (1), Reforestation (2), Resilience Building (1)"
s="Crop Damage (1), Disability (1), Disease/Health Effects (2), Economic and Livelihood Loss (1), Loss of Access to Basic Services (1), School/Education Drop Out (1)"
s="Lack Of Awareness And Education (2), Lack Of Facilities (1), Lack Of Government Action (1), Lack Of Resources (3)"
s="Awareness Raising  Education and Training (1), Drainage Channels (1), Health Promotion (1), Investment in Infrastructure Improvement and Mitigation Works (3), Maintain Basic Services (Medical and Other) (1)"
s="Building Destruction (3), Commercial Loss (3), Crop Damage (10), Disease/Health Effects (1), Economic and Livelihood Loss (3), Environmental effects (5), Erosion (2), Flooding (1), Food Insecurity (1), Impact on Biodiversity (2), Infrastructure Damage (10), "
s="Building Destruction (3), Commercial Loss (3), Crop Damage (10), Disease/Health Effects (1), Economic and Livelihood Loss (3), Environmental effects (5), Erosion (2), Flooding (1), Food Insecurity (1), Impact on Biodiversity (2), Infrastructure Damage (10), Livestock Loss (1), Loss of Clean Water Sources (1), Reduction In Irrigation (1), School/Education Drop Out (1)"
s="Communication Issues (1), Economic Policies (9), Family Problem/ Issues (1), Lack Of Access To Technology (2), Lack Of Accessibility (1), Lack Of Awareness And Education (8), Lack Of Employment (1), Lack Of Government Commitment (2), Lack Of Initiative (1), Lack Of Land Surveying And Planning (1), Lack Of Opportunity/Time (1), Lack Of Policies (1), Lack Of Preparedness (1), Lack Of Resources (4), Lack Of Risk Awareness And Planning (2), Poverty (1)"
s="Awareness Raising  Education and Training (3), Climate Change Adaptation (1), Climate Change Mitigation (1), Dam/Dyke Building (14), Disaster Preparedness (5), Drainage Channels (1), Early Warning Systems (EWS) (1), Implementation of policies (1), Investment in Infrastructure Improvement and Mitigation Works (3), Livelihood Diversification (1), Raising Homes (1), Reconstruction (2), Reforestation (8), Resilience Building (1), Water and Sanitation Programme (1)"
s="Awareness Raising  Education and Training (3), Climate Change Adaptation (1), Climate Change Mitigation (1), Dam/Dyke Building (14), Disaster Preparedness (5), Drainage Channels (1), Early Warning Systems –EWS- (1), Implementation of policies (1), Investment in Infrastructure Improvement and Mitigation Works (3), Livelihood Diversification (1), Raising Homes (1), Reconstruction (2), Reforestation (8), Resilience Building (1), Water and Sanitation Programme (1)"
s="Awareness Raising  Education and Training (1), Drainage Channels (1), Health Promotion (1), Investment in Infrastructure Improvement and Mitigation Works (3), Maintain Basic Services -Medical and Other- (1)"
s="Awareness Raising  Education and Training (1), Climate Change Adaptation (1), Climate Change Mitigation (1), Dam/Dyke Building (6), Disaster Preparedness (2), Drainage Channels (1), Early Warning Systems EWS (1), Investment in Infrastructure Improvement and Mitigation Works (1), Reforestation (2), Resilience Building (1)"
alist= s.split(",")

slist = sorted(alist, key=lambda x: int(x.partition('(')[2].partition(')')[0]), reverse=True)

ss = ", ".join(slist)

print ss

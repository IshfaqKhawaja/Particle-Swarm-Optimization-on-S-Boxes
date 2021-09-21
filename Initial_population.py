def renyi_map(c,xr,m):
	for i in range(m):
		xr=(c*xr)%1
	return xr


def initial_s_box(n,c,xr):
	total_no=2**n
	s_box=[0 for i in range(total_no)]
	map_dict={}
	for i in range(total_no):
		xr = renyi_map(c,xr,1)
		s_box[i]=xr
		map_dict[xr]=i
	s_box.sort()
	for i in range(total_no):
		s_box[i] = map_dict[s_box[i]]
	return s_box,xr


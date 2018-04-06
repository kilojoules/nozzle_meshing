// Author: Robert Lee
// Email: rlee32@gatech.edu
// All units are metric.
// Geometry follows that specified on:
// http://www.grc.nasa.gov/WWW/wind/valid/cdv/cdv.html
//Inputs
normal_cells = 61;
axis_cells = 101;
samples = 50000; // points to use in BSpline of nozzle wall.
bump = 1; // controls concentration near wall and centerline.
// Constants
itm = 0.0254; // inch to meter.
i2tm2 = itm*itm; // in^2 to m^2
// Subroutines
// Takes a position and gives the area according to the prescribed geometry.
// Input: x
// Output: a
Function area
If ( x < 10 * NUM4 )
// a = i2tm2 * ( 1.75 - 0.75 * Cos( ( 0.2 * x / itm - 1.0 ) * Pi ) );
// Else
// a = i2tm2 * ( 1.25 - 0.25 * Cos( ( 0.2 * x / itm - 1.0 ) * Pi ) );
a = i2tm2 * ( NUM1 + (NUM2) * Cos( ( x /(10 * NUM4) - 1.0 ) * Pi ) );
//a = i2tm2 * (0.375  - -0.125 * Cos( ( x / itm - 1.0 ) * Pi ) );
Else
a = i2tm2 * ( NUM1 + NUM2 + NUM3 * (Cos( x * Pi /(10 * NUM4) - Pi ) - 1) );
//a = i2tm2 * ( 1.25 - 0.25 * Cos( ( 0.2 * x / itm - 1.0 ) * Pi ) );
EndIf
Return
// Takes a position and computes the corresponding radius.
// Input: x
// Output: r
Function radius
Call area;
r = Sqrt( a / Pi );
Return
// Draw Points.
ce = 0;
Point(ce++) = { 0, 0, 0 }; axis_start = ce;
Point(ce++) = { 10*itm, 0, 0 }; axis_end = ce;
x = 0;
Call radius;
Point(ce++) = { x*itm, r, 0 }; wall_start = ce;
x = 10;
Call radius;
Point(ce++) = { x*itm, r, 0 }; wall_end = ce;
wall_points[] = {};
For k In {1:samples-2}
//x = k * 10*itm / (samples-1);
x = k * 10 / (samples-1);
Call radius;
Point(ce++) = { x*itm, r, 0 };
wall_points[] += ce;
EndFor
// Draw Lines.
BSpline(ce++) = { wall_start, wall_points[], wall_end }; wall = ce;
Line(ce++) = {axis_start, axis_end}; axis = ce;
Line(ce++) = {axis_start, wall_start}; inlet = ce;
Line(ce++) = {axis_end, wall_end}; outlet = ce;
// Make surfaces.
Line Loop(ce++) = { axis, outlet, -wall, -inlet };
loop = ce;
Plane Surface(ce++) = loop; surf = ce;
// Specify structured meshing.
Transfinite Line{ wall, axis } = axis_cells + 1;
Transfinite Line{ inlet, outlet } = normal_cells + 1 Using Bump bump;
Transfinite Surface{ surf };
Recombine Surface{ surf };
// Define names of physical surfaces.
Physical Surface("nozzle") = {203};
Physical Surface("outlet") = {206};
Physical Surface("inlet") = {205};
Physical Surface("bottom") = {204};
Physical Surface("Fluid") = {208};


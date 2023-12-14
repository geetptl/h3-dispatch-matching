create table riders
(
    id       serial primary key,
    location point
);

create table drivers
(
    id       serial primary key,
    location point
);


insert into riders (location)
values (point(40.7128, -74.0060));
insert into riders (location)
values (point(40.7282, -74.0776));
insert into riders (location)
values (point(40.7357, -74.1724));
insert into riders (location)
values (point(41.0534, -73.5387));
insert into riders (location)
values (point(40.9312, -73.8987));
insert into riders (location)
values (point(41.0330, -73.7629));
insert into riders (location)
values (point(40.7434, -74.0324));
insert into riders (location)
values (point(41.3082, -72.9282));
insert into riders (location)
values (point(41.3948, -73.4540));
insert into riders (location)
values (point(40.9168, -74.1718));
insert into riders (location)
values (point(41.1177, -73.4082));
insert into riders (location)
values (point(40.6631, -74.2107));
insert into riders (location)
values (point(41.1865, -73.1958));
insert into riders (location)
values (point(40.9126, -73.8371));
insert into riders (location)
values (point(40.8259, -74.2090));
insert into riders (location)
values (point(40.9115, -73.7822));
insert into riders (location)
values (point(41.0514, -73.5367));
insert into riders (location)
values (point(40.8682, -73.4257));
insert into riders (location)
values (point(40.7968, -74.4815));
insert into riders (location)
values (point(41.0262, -73.6282));


insert into drivers (location)
values (point(41.0907, -73.9179));
insert into drivers (location)
values (point(40.5885, -73.6579));
insert into drivers (location)
values (point(40.3573, -74.6672));
insert into drivers (location)
values (point(41.0717, -73.4837));
insert into drivers (location)
values (point(41.0329, -73.7625));
insert into drivers (location)
values (point(41.2307, -73.0642));
insert into drivers (location)
values (point(40.6496, -74.3476));
insert into drivers (location)
values (point(40.9875, -73.7801));
insert into drivers (location)
values (point(41.1792, -73.1894));
insert into drivers (location)
values (point(40.7440, -74.0368));

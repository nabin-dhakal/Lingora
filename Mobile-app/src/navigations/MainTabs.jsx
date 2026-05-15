import IonIcons from '@expo/vector-icons/Ionicons';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import React from 'react';
import HomeScreen from '../screens/HomeScreen';


const MainTabs = () => {
    const Tab = createBottomTabNavigator();

    return (
            <Tab.Navigator
                screenOptions={({ route }) => ({
                    tabBarIcon: ({ focused, color, size }) => {
                        let iconName;

                        if (route.name === 'Home') {
                            iconName = focused ? 'home' : 'home-outline';
                        } else if (route.name === 'Profile') {
                            iconName = focused ? 'person' : 'person-outline';
                        } else if (route.name === 'Leaderboard') {
                            iconName = focused ? 'trophy' : 'trophy-outline';
                        }

                        return <IonIcons name={iconName} size={size} color={color} />;
                    },
                    tabBarActiveTintColor: '#1CB0F6',
                    tabBarInactiveTintColor: 'gray',
                    headerShown: false,
                })}
            >
                <Tab.Screen name="Home" component={HomeScreen} />
            </Tab.Navigator>
    );
};

export default MainTabs;
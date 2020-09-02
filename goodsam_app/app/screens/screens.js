import * as React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import Post from './Post'
import Home from './home'
const MainStack = createStackNavigator();


class Screens extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
        }

    }

    render() {
        console.log("The current screen is: " + this.props.screen)
        return (
            <NavigationContainer>
               <MainStack.Navigator initialRouteName="home">
                    <MainStack.Screen
                        name="home"
                        component={Home}
                    />
                    <MainStack.Screen
                        name="post"
                        component={Post}
                    />
                </MainStack.Navigator>
            </NavigationContainer>
        );
    }
}

export default Screens;

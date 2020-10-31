import React, { Component } from 'react';
import  AsyncStorage  from '@react-native-community/async-storage';
import {
  TouchableOpacity,
  SafeAreaView,
  StyleSheet,
  ScrollView,
  View,
  Text,
  StatusBar,
  Image,
  Dimensions,
} from 'react-native';
import IconAntDesign from 'react-native-vector-icons/AntDesign'

import {
  Header,
  LearnMoreLinks,
  Colors,
  DebugInstructions,
  ReloadInstructions,
} from 'react-native/Libraries/NewAppScreen';
import firebase from 'firebase/app'
import 'firebase/auth'
import 'firebase/firestore'
export default class Home extends Component {

  constructor(props) {
    super(props);

    this.state = {
      email: [],
      password: '',
      userName: 'hey',
      token: "",
      items: [],

    };
  }

  componentDidMount() {










    /*firebase.firestore().collection("cities").doc("LA").set({
    name: "Los Angeles",
    state: "CA",
    country: "USA"
})
.then(function() {
    console.log("Document successfully written!");
})
.catch(function() {
    console.error("Error writing document: ");
});
console.log("hey")*/


  }

  render(



  ) {
    const { navigate } = this.props.navigation;
    
    /**
    * @param {string} userId
    * @returns {Promise} Object: { emailAddress, messagesTotal, threadsTotal , historyId }
    */




    return (
      <SafeAreaView style={styles.body}>


          <View >
          <View style={styles.imgContainer}>
          <Image style={styles.Image}
        source={require('./logo1.png')}
      />

      <Image style={styles.Image2}
          source={require('./logo2.png')}
        />
        </View>
        <TouchableOpacity
         style={styles.sectionContainer}
         onPress={() => this.props.navigation.navigate('login')}
       >
         <Text style={styles.Text}>Login</Text>
       </TouchableOpacity>

        </View>
        <View style={styles.or}>
        <Text>OR</Text>
        </View>

      <TouchableOpacity
       style={styles.sectionContainer2}
       onPress={() => this.props.navigation.navigate('signup')}
     >
       <Text style={styles.Text}>Signup</Text>
     </TouchableOpacity>

      </SafeAreaView >

    );
  }
}
var width = Dimensions.get('window').width;
var height = Dimensions.get('window').height;
const styles = StyleSheet.create({
  scrollView: {

  },
  button: {
    alignItems: "center",
    backgroundColor: "#DDDDDD",
    padding: 10
  },
  engine: {
    position: 'absolute',
    right: 0,
  },
  Text : {
    color: 'white',
    fontWeight:'bold',
  },
  or:{
    marginTop: 25,
    alignItems:'center'
  },
  Image : {
    width: width *.5,
    height:30,
    height:height*.1,
    resizeMode: 'contain',
    paddingBottom: 0,
  },
  imgContainer: {
    marginTop:width*.4,
    alignItems:'center'
  },
  sectionContainer : {
      marginTop: 50,
      borderRadius: 50,
      alignItems: 'center',
      marginLeft: width*.15,
      height:50,
      width: width * .7,
      backgroundColor: 'orange',
      justifyContent: 'center',

  },
  sectionContainer2 : {
      marginTop: 25,
      borderRadius: 50,
      alignItems: 'center',
      marginLeft: width*.15,
      height:50,
      width: width * .7,
      backgroundColor: 'orangered',
      justifyContent: 'center',

  },
  Image2 : {
    marginTop:0,
    height:height*.1,
    width: width *.9,
    resizeMode: 'contain'
  },
  body: {

    height:height,
    backgroundColor: 'white',
  },

});

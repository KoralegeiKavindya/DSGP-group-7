import React from "react";
import { View} from "react-native";
import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import HomeScreen from "./HomeScreen";
import brownspot from "./brownspot";
import styles from "./styles";
import Recomendations from "./recomendations";
import Mild_Brownspot from "./Mild_Brownspot";
import Severe_Brownspot from "./Severe_Brownspot";
import Gojarawalu_remedy from "./Gojarawalu_remedy";
import LoginScreen from './screens/LoginScreen';
import HomeScreen1 from './screens/HomeScreen1';
import chatbot from "./chatBot";
import Gojarawalu from "./Gojarawalu";

const Stack = createNativeStackNavigator();

export default function App(){
  
  return <View style={styles.container}> 
  <NavigationContainer>
    <Stack.Navigator>
      <Stack.Screen options={{ headerShown: false }} name="Login" component={LoginScreen} />
      <Stack.Screen name="Logout" component={HomeScreen1} />
      <Stack.Screen name="Home" component={HomeScreen}/>
      <Stack.Screen name="brownspot" component={brownspot}/>
      <Stack.Screen name="gojarawalu" component={Gojarawalu}/>
      <Stack.Screen name="chatbot" component={chatbot}/>
      <Stack.Screen name="recomendations" component={Recomendations}/>
      <Stack.Screen name="Mild_Brownspot" component={Mild_Brownspot}/>
      <Stack.Screen name="Severe_Brownspot" component={Severe_Brownspot}/>
      <Stack.Screen name="Gojarawalu_remedy" component={Gojarawalu_remedy}/>
    </Stack.Navigator>
  </NavigationContainer>

  </View>;
};